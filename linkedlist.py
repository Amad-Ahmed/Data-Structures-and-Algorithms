class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data=None):
        # creating a function of node class and storing data
        #  along with address of head in next position
        node = Node(data,self.head)
        
        # Then I reappoint the head to the current inserted node object
        self.head = node
        

    def insert_at_end(self,data=None):
        if(self.head == None):
            self.head=Node(data,None)
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    
    def printList(self):
        if (self.head == None):
            print("List is empty")
            return
        # else create iterator and print the list
        itr = self.head
        liststr = ""

        while itr:
            liststr += str(itr.data) + " --> "
            itr = itr.next
        
        print(liststr)
    
    def insert_value(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def return_length(self):
        length = 0
        itr = self.head
        while itr:
            length+=1
            itr=itr.next
        return length

    def remove_at(self,index):
        if index<0 or index>self.return_length():
            raise Exception("Invalid index")
        if (index == 0):
            self.head = self.head.next
            return

        index_check = 0
        itr = self.head
        while itr:
            if (index_check == index-1):
                itr.next = itr.next.next
                break

            index_check+=1
            itr=itr.next

    def insert_at(self,index,data):
        if index<0 or index>self.return_length():
            raise Exception("Invalid index")
        if (index == 0):
            self.insert_at_beginning(data)
            return
        
        index_check = 0
        itr = self.head
        while itr:
            if (index_check == index-1):
                node = Node(data)
                node.next = itr.next.next
                itr.next = node
                break
            index_check+=1
            itr= itr.next
    def insert_after_value(self,data_after,data_to_insert):
        itr = self.head
        while itr:
            if (itr.data == data_after):
                node = Node(data_to_insert)
                node.next = itr.next
                itr.next = node
                break
            itr=itr.next
    
    def remove_by_value(self,data):
        itr = self.head
        prev = 0
        while itr:
            if (itr.data == data):
                # If head node
                if (itr == self.head):
                    self.head = itr.next
                    break
                else:
                    prev.next = itr.next
                    break

            prev = itr
            itr = itr.next
            





            


if __name__ == '__main__':
    linkedList = LinkedList()
    linkedList.insert_at_beginning(1)
    linkedList.insert_at_beginning(2)
    linkedList.insert_at_beginning(3)
    linkedList.insert_at_end(5)
    linkedList.return_length()
    linkedList.printList()


