class NFA:
    current_state = None
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state
        return
        
    def transition_to_state_with_input(self, input_value):
        kq = set()
        for item in self.current_state:
            if ((item, input_value) not in self.transition_function.keys()):
                continue
            else:
                kq = kq | self.transition_function[(item, input_value)]
            self.current_state = kq
            return 
            
    def in_accept_state(self):
        return self.current_state & self.accept_states
    
    def go_to_initial_state(self):
        self.current_state = self.start_state
        return
        
    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        print("trang thai bat dau la: ", self.current_state)
        print("chuoi can kiem tra la: ", input_list)
        for inp in input_list:
        # kiem tra tung ky tu co thuoc bo chu cai nhap
            if inp not in alphabet:
                print("ton tai ky tu khong thuoc bo chu cai nhap")
                return
            else:
                self.transition_to_state_with_input(inp)
            return self.in_accept_state()

states = {0, 1, 2, 3, 4}
alphabet = {'0', '1'}
start_state = {0}
accept_states = {2, 4}       
tf = dict() 
tf[(0, '0')] = {0, 3}
tf[(0, '1')] = {0, 1}
tf[(1, '1')] = {2}
tf[(2, '0')] = {2}
tf[(2, '1')] = {2}
tf[(3, '0')] = {4}
tf[(4, '0')] = {4}
tf[(4, '1')] = {4}

d = NFA(states, alphabet, tf, start_state, accept_states)
print("Nhap chuoi can kiem tra: ")
inp_program = list(input())
result = d.run_with_input_list(inp_program)

if len(result) == 0:
    print("Chuoi khong thuoc ngon ngu sinh boi NFA da cho")
else:
    print("Chuoi thuoc ngon ngu sinh boi NFA da cho")