class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for i in range(len(operations)):
            if operations[i] == '+' and i > 1:
                record.append(record[-1] + record[-2]) 
            elif operations[i] == 'D' and i > 0:
                record.append(record[-1] * 2)
            elif operations[i] == 'C' and i > 0:
                record.pop()
            else: 
                record.append(int(operations[i]))

        
        ssum = 0
        for i in range(len(record)):
            
            ssum+=record[i]
        return ssum
