from itertools import permutations 
  
amps = list(permutations([0, 1, 2, 3, 4]))
#amps = [[4,3,2,1,0]]
#print(len(phases))

program = []
pointer = 0

_in = 0
_out = 0

_max = 0
_max_phases = None

def main():
    global program, pointer, _in, _out, _max, _max_phases

    program = read()

    for phases in amps:
        _out = 0
        for phase in phases:
            #print("Phase: " + str(phase))
            pointer = 0
            _in = phase
            _program = program.copy()

            while pointer < len(_program):
                try:
                    inst = str(_program[pointer]).rjust(2, '0')
                    opcode = int(inst[len(inst) - 2] + inst[len(inst) - 1])
                    OPCODE[opcode](_program)
                except KeyError:
                    print("KeyError")
                    break
                except SystemExit:
                    break
        
        if _out > _max:
            _max = _out
            _max_phases = phases
        
        #print("Phases: " + str(phases) + " - Output: " + str(_out))
    print("Max Phase: " + str(_max_phases)  + " - Output: " + str(_max))

def _get_params(program, num_params):
    global pointer
    modes = [int(val) for val in str(program[pointer]).rjust(num_params + 2, '0')]
    params = []
    for i in range(num_params - 1, -1, -1):
        pointer += 1
        params.append(PARAM[int(modes[i])](program, pointer))
    return params

def _write(program, val):
    global pointer
    program[program[pointer]] = val
    pointer += 1

def _add(program):
    params = _get_params(program, 3)
    _write(program, params[0] + params[1])

def _multiply(program):
    params = _get_params(program, 3)
    _write(program, params[0] * params[1])

def _input(program):
    global _in
    _get_params(program, 1)
    #_write(program, int(input("Provide input: ")))
    #print("In: " + str(_in))
    _write(program, _in)
    _in = _out

def _output(program):
    global pointer, _in, _out
    params = _get_params(program, 1)
    #print("Out: " + str(params[0]))
    _out = params[0]
    pointer += 1

def _jump(program, do_jump):
    global pointer
    params = _get_params(program, 2)
    pointer = params[1] if (params[0] != 0) == do_jump else pointer + 1

def _less_than(program):
    params = _get_params(program, 3)
    _write(program, 1 if params[0] < params[1] else 0)

def _equals(program):
    params = _get_params(program, 3)
    _write(program, 1 if params[0] == params[1] else 0)

def _exit():
    #print("Exit")
    raise SystemExit

OPCODE = {
    1: (lambda program: _add(program)),
    2: (lambda program: _multiply(program)),
    3: (lambda program: _input(program)),
    4: (lambda program: _output(program)),
    5: (lambda program: _jump(program, True)),
    6: (lambda program: _jump(program, False)),
    7: (lambda program: _less_than(program)),
    8: (lambda program: _equals(program)),
    99: (lambda program: _exit())
}

PARAM = {
    0: (lambda program, pos: program[program[pos]]),
    1: (lambda program, pos: program[pos])
}

def read():
    input = open("input.txt", "r")
    return [int(i) for i in input.read().split(",")]

if __name__ == "__main__":
    main()