import array

class DynamicArray:
    def __init__(self, capacity: int = 2):
        self.__cap = capacity
        self.__size = 0                           ########## elementneri qanak
        self.__arr = array.array('i', [0] * self.__cap)

    def is_empty(self):
        if self.__size == 0:
            return True
        return False

    def insert(self, position: int, data: int):
        if position < 0 or position > self.__size:
            raise IndexError("Out of range")
        
        if self.__size == self.__cap:
            self.resize(self.__cap * 2)
        
        for  i in range(self.__size - 1, position, -1):
            self.__arr[i] = self.__arr[i-1]
        self.__arr[position] = data
        self.__size += 1

    def _resize(self, new_cap):
        tmp = array.array('i', [0] * new_cap)
        for i in range(self.__size):
            tmp[i] = self.__arr[i]
        self.__arr = tmp
        self.__cap = new_cap

    def reserve(self, new_cap):
        if new_cap > self.__cap:
            self._resize(new_cap)

    def push_back(self,data: int):
        if self.__size == self.__cap:
            self._resize(self.__cap * 2)
        self.__arr[self.__size] = data
        self.__size += 1

    def emplace(self, position: int, data: int):
        if position < 0 or position > self.__size - 1:
            raise IndexError("Out of range")
        self.__arr[position] = data

    def pop_back(self):
        if self.__size == 0:
            return IndexError("Out uf range")
        self.__arr[self.__size - 1] = 0
        self.__size -= 1
        if self.__size > 0 and self.__size == self.__cap // 4:
            self._resize(self._capacity // 2)

    def remove(self, index: int):
        if index < 0 or index > self.size - 1:
            raise IndexError("Out of range")
        
        for i in range(index, self.__size):
            self.__arr[i] = self.__arr[i+1]
        self.__size -= 1

    def size(self):
        return self.__size

    def include(self, element: int) -> bool:
        for i in range(self.__size):
            if self.__arr[i] == element:
                return True          
        return False
    
    def capacity(self):
        return self.__cap
    
    def shrink_to_fit(self):
        if self.__size < self.__cap:
            self.resize(self.__size)

    def clear(self):
        for i in range(self.__size):
            self.__arr[i] = 0
        self.__size = 0

    def __assign__(self, other):
        if self is not other:  
            self.__cap = other.__cap
            self.__size = other.__size
            self.__arr = array.array('i', [0] * self.__cap)
            for i in range(other.__size):
                self.__arr[i] = other.__arr[i]

    def __getitem__(self,position):
        if position < 0 or position > self.__size - 1:
            raise IndexError("Out of range")
        return self.__arr[position]

    def __setitem__(self, position: int, data: int):
        if not(0 <= position < self.__size):
            raise IndexError("Out of range")
        self.__arr[position] = data
    
    def __str__(self):
        data = ""
        for i in range(self.__size):
            data += (str(self.__arr[i]) + " ")
        return data
    
ob = DynamicArray()
ob.push_back(15)
ob.push_back(24)
ob.push_back(10)
print(ob)
# print(ob.include(0))
# ob.pop_back()
# ob.emplace(1,7)
# print(ob.size())

# print(ob[1]) 

# ob.clear()

ob1 = DynamicArray()
ob1.push_back(48)
ob1.push_back(65)
ob1.push_back(56)
print(ob1)

ob1 = ob
print(ob1)

