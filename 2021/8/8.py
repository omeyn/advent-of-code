import os

os.chdir('2021/8')

class Decoder:
    def __init__(self, signals):
        self.lookup = {}
        self.num_lookup = {}
        self.processed_signals = 0
        for signal in signals:
            # print("adding signal {}".format(signal))
            match len(signal):
                case 2:
                    self.update_lookup(1, signal)
                case 3:
                    self.update_lookup(7, signal)
                case 4:
                    self.update_lookup(4, signal)
                case 7:
                    self.update_lookup(8, signal)
        
        while self.processed_signals < len(signals):
            print("Got {} of {} signals processed".format(self.processed_signals, len(signals)))
            for signal in signals:
                if signal in self.lookup:
                    # print("Found signal {} in lookup {}, skipping".format(signal, self.lookup))
                    continue
                # print("Checking signal {}".format(signal))
                # print(self.lookup)
                match len(signal):
                    case 5:
                        # 2, 3, 5
                        # if self.one_from_three([2,3,5], signal):
                        #     break

                        # 3 is direct from 7
                        if set(self.num_lookup[7]).issubset(set(signal)):
                            self.update_lookup(3, signal)
                            break

                        # 9 - 1 and 5 - 1 are the same

                        # 9-7 and 5-7 are the same
                        # if 9 in self.num_lookup and 7 in self.num_lookup:
                        #     partial = set(self.num_lookup[9]) - set(self.num_lookup[7])
                        #     test = set(signal) - set(self.num_lookup[7])
                        #     if partial == test:
                        #         self.update_lookup(5, signal)
                        #         break

                        # 5 contains  (4-1), but 2 doesn't
                        print("checking for 5 vs 2")
                        partial = set(self.num_lookup[4]) - set(self.num_lookup[1])
                        print("4 -1 is {}".format(partial))
                        if partial.issubset(set(signal)):
                            print("found {} in {} so this is 5".format(partial, signal))
                            self.update_lookup(5, signal)
                            break
                        else:
                            print("did not find {} in {} so this is 2".format(partial, signal))
                            self.update_lookup(2, signal)
                            break
                        
                    case 6: 
                        # 9, 0, 6
                        # self.one_from_three([0,6,9], signal)

                        if set(self.num_lookup[1]).issubset(set(signal)):
                            if set(self.num_lookup[4]).issubset(set(signal)):
                                # 9 contains 1 and 4
                                print("{} contains 1 {} and 4 {} so this is 9".format(signal, self.num_lookup[1], self.num_lookup[4]))
                                self.update_lookup(9, signal)
                                break
                            else:
                                # 0 contains 1 and not 4
                                # print("deducing 9,6,0 - contains 1 and not 4 {}".format(signal, self.num_lookup[4]))
                                print("{} contains 1 {} and not 4 {} so this is 0".format(signal, self.num_lookup[1], self.num_lookup[4]))
                                self.update_lookup(0, signal)
                                break
                        else:
                            # 6 does not contain 1
                            print("{} does not contain 1 {} so this is 6".format(signal, self.num_lookup[1]))
                            self.update_lookup(6, signal)
                            break

        # print("built lookup: {}".format(self.lookup))

    def one_from_three(self, ops, signal):
        if ops[0] in self.num_lookup and ops[1] in self.num_lookup:
            print("got {} and {} so {} must be {}".format(ops[0],ops[1],signal,ops[2]))
            self.update_lookup(ops[2], signal)
            return True
        elif ops[0] in self.num_lookup and ops[2] in self.num_lookup:
            print("got {} and {} so {} must be {}".format(ops[0],ops[2],signal,ops[1]))
            self.update_lookup(ops[1], signal)
            return True
        elif ops[1] in self.num_lookup and ops[2] in self.num_lookup:
            print("got {} and {} so {} must be {}".format(ops[1],ops[2],signal,ops[0]))
            self.update_lookup(ops[0], signal)
            return True
        
        return False

    def update_lookup(self, num, signal):
        print("Updating lookup with {} = {}".format(signal, num))
        self.lookup[signal] = num
        self.num_lookup[num] = signal
        self.processed_signals += 1

    def decode(self, digit):
        result = None
        for key in self.lookup.keys():
            if set(key) == set(digit):
                result = self.lookup[key];
        # print("lookup {} result is {}".format(digit, result))
        return result

def star1():
    f = open("8.input", "r")
    # f = open("8-test.input", "r")
    # f = open("8-test-1.input", "r")
    special_count = 0
    for line in f:
        raw_signals = line.split("|")[0].split()
        print(raw_signals)
        decoder = Decoder(raw_signals)
        raw_outputs = line.split("|")[1].split()
        # print(raw_outputs)
        code = ""
        for output in raw_outputs:
            result = decoder.decode(output)
            code = code + str(result)
            # if result:
                # special_count += 1
                # print(result)
        # print("##################### GOT CODE " + code)
        special_count += int(code)
    print(special_count)


        


    


star1()