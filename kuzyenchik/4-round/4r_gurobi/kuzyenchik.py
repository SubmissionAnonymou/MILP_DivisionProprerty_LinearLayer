


from gurobipy import *
import time
from AESLike import *
from SolveModel import *
from newMatrixModel import *
from dependency import *
from constants import Matrix
import multiprocessing as mp
import shutil
import os



machine = os.uname()[1]

_logDir = '/tmp/kuzyenchik_4_round_gurobi/'

if not os.path.exists(_logDir):
    try:
        os.mkdir(_logDir)
    except OSError:
        print ("Creation of the directory %s failed" % _logDir)
        exit()
    else:
        print ("Successfully created the directory %s " % _logDir)
    



ISTIMELIMIT = 0
TIMELIMIT = 3600
ISThREADS = 1
Threads = 48
ISNodefileDir = 1
NodefileStart = 0.5
UseOptimize = 1


print("Finish setting gurobi parameter")

def printResult(inputDP, balanceBits):
    activebits = inputDP.count('1')
    fileobj = open(filename_result, "a", buffering=1)
    print('# of rounds: %i' % Rounds + " , activebits:%i " % activebits + ", Input DP: " + inputDP)
    print("balanced bits: " + str(len(balanceBits)) + ' ' + str(balanceBits))
    fileobj.write('# of rounds: %i' % Rounds + " , activebits:%i " % activebits + ", Input DP: " + inputDP + "\n")
    fileobj.write("balanced bits: " + str(len(balanceBits)) + ' ' + str(balanceBits) + "\n")
    fileobj.close()


def WriteModel(constraints, variables, objective, filename_model):
    file_co = open(filename_model, 'w+')
    if UseOptimize:
        file_co.write('Minimize\n')
        file_co.write(' + '.join(objective) + '\n')
    file_co.write('Subject To\n')
    for enq in constraints:
        file_co.write(enq + '\n')
    file_co.write('Binary\n')
    for v in variables:
        file_co.write(v + '\n')
    file_co.close()


def createModel(Rounds, inputDP, filename_model):
    variables = []
    constraints = []
    InputOutputVariablesLinearLayer = []
    InputVariables = []
    OutputVariables = []
    

    # round 0 MixColumn
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    Z = ShiftRow(CreateStateVariable('y', blocksize//wordSize, wordSize, 0))
    Xout = CreateStateVariable('x', blocksize//wordSize, wordSize, 1)
    inputDP_column = [inputDP[i:i+ColSize] for i in range(0, blocksize//wordSize, ColSize)]
    Z_column = [Z[i:i+ColSize] for i in range(0, blocksize//wordSize, ColSize)]
    Xout_column = [Xout[i:i+ColSize] for i in range(0, blocksize//wordSize, ColSize)]
    for ColIndex in range(len(inputDP_column)):
        currentColDP = ''.join(inputDP_column[ColIndex])
        if '0' in currentColDP:
            u = list(map(int, currentColDP))
            v = [1] * len(u)
            _subMatrix = subMatrix(Matrix, u, v)
            MatrixConstraints = linearDependent(_subMatrix)
            tmpVariables , tmpConstraints, tmpInputOutputVariablesLinearLayer = ConstraintsByMixColumnNew(Z_column[ColIndex], Xout_column[ColIndex], 0, ColIndex, MatrixConstraints)    
            variables += words2bits(Z_column[ColIndex])
            variables += tmpVariables
            constraints += tmpConstraints
            InputOutputVariablesLinearLayer += [tmpInputOutputVariablesLinearLayer]
            InputVariables += words2bits(Z_column[ColIndex])   
        else:
            InputVariables += words2bits(Xout_column[ColIndex])   
    
    constraints = ['%s = %s' %(a, b) for a, b in zip(InputVariables, ''.join(inputDP))] + constraints
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    for r in range(1, Rounds):
        tmpVariables, tmpConstraints, tmpInputOutputVariablesLinearLayer = ConstraintByRound(r)
        variables += tmpVariables
        constraints += tmpConstraints
        InputOutputVariablesLinearLayer += tmpInputOutputVariablesLinearLayer
        
    
    Xout = CreateStateVariable('x', blocksize//wordSize, wordSize, Rounds)
    variables += sum(Xout, [])
    OutputVariables = words2bits(Xout)
    WriteModel(constraints, variables, OutputVariables, filename_model)

    model = read(filename_model)
    model._InputVariables = getVarsByName(model, InputVariables)
    model._OutputVariables = getVarsByName(model, OutputVariables)
    model._InputOutputVariablesLinearLayer = [(getVarsByName(model, X), getVarsByName(model, Y)) for X, Y in InputOutputVariablesLinearLayer]

    return model






def ConstraintByRound(r):
    NBytesState = blocksize//wordSize
    Xin = CreateStateVariable('x', NBytesState, wordSize, r)
    Y = CreateStateVariable('y', NBytesState, wordSize, r)
    Xout = CreateStateVariable('x', NBytesState, wordSize, r + 1)

    Variables = []
    Constraints = []

    Variables += sum(Xin, [])  # convert 2d to 1d
    Variables += sum(Y, [])

    tmpConstraints = ConstraintsBySboxLayer(Xin, Y)
    Constraints += tmpConstraints

    Z = ShiftRow(Y)

    tmpVariables, tmpConstraints, InputOutputVariablesLinearLayer = ConstraintsByLinearLayer(Z, Xout, ColSize, r)
    Variables += tmpVariables
    Constraints += tmpConstraints

    return (Variables, Constraints, InputOutputVariablesLinearLayer)



if __name__ == "__main__":
    
    
    # if (len(sys.argv) != 2):
    #     print("args sould be 1")
    #     exit()
    
    # InactiveByeIndx = int(sys.argv[1])
    InactiveByeIndx = 0


    time_start = time.time()
    

    Rounds = 4
    blocksize = 128
    wordSize = 8
    ColSize = 16
    
    Blockcipher = "kuzyenchik"

    
    filename_model = "tmp/" + Blockcipher + "_" + str(Rounds) + "r" + "_InactiveByeIndx_%02i" %InactiveByeIndx + "_%s" %(str(time.time())) +  ".lp"
    filename_result = "tmp/" + Blockcipher + "_" + str(Rounds) + "r" + "_InactiveByeIndx_%02i" %InactiveByeIndx + "_Result_%s_" %("optimize" if UseOptimize else "bitbybit") + str(Rounds) + "r" + "_%s_" %machine.split('.')[0] + "_%s" %(str(time.time())) + ".txt"



    logDir = _logDir + "%s_%ir_%03i/" %(Blockcipher, Rounds, InactiveByeIndx)
    
    if not os.path.exists(logDir):
        try:
            os.mkdir(logDir)
        except OSError:
            print ("Creation of the directory %s failed" % logDir)
            exit()
        else:
            print ("Successfully created the directory %s " % logDir)


    fileobj = open(filename_result, "a", buffering=1)


    __inputDP = ['1' * wordSize] * (blocksize//wordSize)
    __inputDP[InactiveByeIndx] = '0' * wordSize
    inputDP = list(__inputDP)
 



    m = createModel(Rounds, inputDP, filename_model)

    m._Rounds = Rounds
    m._blocksize = blocksize
    m._Blockcipher = Blockcipher
    m._filenameResult = filename_result
    m.setParam("LogToConsole", 0)
    
    if ISThREADS:
        m.setParam("Threads", Threads)
    if ISNodefileDir:
        NodefileDir = logDir[:-1] # remove last /
        m.setParam("NodefileDir", NodefileDir)
        m.setParam("NodefileStart", NodefileStart)

    fileobj.write("InactiveByeIndx: %02i\n" %(InactiveByeIndx))
        
    logFile = logDir + machine.split('.')[0] + "_" + m._Blockcipher + "_Intgral_%02i_%s" % (Rounds, str(time.time()))
    m.setParam("LogFile", logFile)
    fileobj.write("Log: %s\n" % logFile)
    print("Log: %s" % logFile, flush=True)
        
        
    fileobj.write("InputDP: %s\n" %(''.join(inputDP)))

    balanceBits = SolveModelOptimize(m)
    printResult(''.join(inputDP), balanceBits)


    time_end = time.time()
    fileobj.write("Total run time: %f Seconds \n" %(time_end - time_start) )
    print("Total run time: %f Seconds " %(time_end - time_start) )

    fileobj.close()

    