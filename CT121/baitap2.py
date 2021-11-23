class DFA:
    current_states = None
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_states = start_state
        return

    def transition_to_state_with_input(self, input_value):
        # nếu không tồn tại đường đi từ trạng thái hiện tại trên input_value
        if((self.current_states, input_value) not in self.transition_function.keys()):
            self.current_states = None
            return
        # tồn tại đường đi từ trạng thía hiên tại trên input_value
        self.current_states = self.transition_function[(self.current_states, input_value)]
        return

    def in_accept_state(self):
        return self.current_states in accept_states
    
    def go_to_initial_state(self):
        self.current_states = self.start_state
        return
    
    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
            continue
        return self.in_accept_state()

states = {0, 1, 2}
alphabet = {'0', '1'}
start_state = 0
accept_states = {0}
tf2 = {(0,'0'):0, (0,'1'):1, (1,'0'):2, (1,'1'):0, (2,'0'):1, (2,'1'):2}
tf = dict()
tf[0, '0'] = 0
tf[0, '1'] = 1
tf[1, '0'] = 2
tf[1, '1'] = 0
tf[2, '0'] = 1
tf[2, '1'] = 2

bai1 = DFA(states, alphabet, tf2, start_state, accept_states)
#test1 = list('10111011')
#test2 = list('1011101')

print("Nhap chuoi can kiem tra")
in_p = list(input())
result = bai1.run_with_input_list(in_p)
if (result==True):
    print("Chuoi thuoc ngon ngu sinh boi DFA da cho")
else:
    print("Chuoi khong thuoc ngon ngu sinh boi DFA da cho")



        