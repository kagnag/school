class DFA:
    current_states = None
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function  = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_states = start_state
        return

    def transition_to_state_with_input(self, input_value):
        # Kiểm tra hàm chuyển trạng thái cho từng phần tử trong current state
        kq = set()
        for item in self.current_states:
            if((item, input_value) not in self.transition_function.keys()):
                continue
            else:
                kq = kq|self.transition_function[(item, input_value)]
        self.current_states = kq
        return

    def in_accept_state(self):
        # return self.current_state in accept_states
        print("tap current_state la: ", self.current_states)
        print("tap trang thai ket thuc la: ", self.accept_states)
        print(self.current_states & self.accept_states)
        return self.current_states & self.accept_states

    def go_to_initital_state(self):
        self.current_states = self.start_state
        return
    
    def run_with_input_list(self, input_list):
        self.go_to_initital_state()
        print("trang thai bat dau la: ", self.current_states)
        print("chuoi can kiem tra la: ", input_list)
        for inp in input_list:
            self.transition_to_state_with_input(inp)
            continue
        return self.in_accept_state()

states = {0, 1, 2}
alphabet = {'0', '1'}
start_state = 0
accept_states = {0}
tf = {(0,'0'):0, (0,'1'):1, (1,'0'):2, (1,'1'):0, (2,'0'):1, (2,'1'):2}


bai1 = DFA(states, alphabet, tf, start_state, accept_states)
test1 = list('10111011')
#test2 = list('1011101')

# print("Nhap chuoi can kiem tra")
# in_p = list(input())
result = bai1.run_with_input_list(test1)
if (result==True):
    print("Chuoi thuoc ngon ngu sinh boi DFA da cho")
else:
    print("Chuoi khong thuoc ngon ngu sinh boi DFA da cho")
