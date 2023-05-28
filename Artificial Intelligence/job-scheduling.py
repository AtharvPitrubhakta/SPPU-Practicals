import heapq


def printjobscheduling(arr):
    n=len(arr)
    
    
    arr.sort(key=lambda x: x[1])
    
    result = []
    maxHeap = []
    
    
    for i in range(n -1, -1, -1):
        
        if i==0:
            slots_available = arr[i][1]
        else:
                slots_available =arr[i][1] - arr[i -1][1]
                
                
        heapq.heappush(maxHeap , (-arr[i][2], arr[i][1], arr[i][0]))
        
        while slots_available and maxHeap:
            
            profit,deadline ,job_id =heapq.heappop(maxHeap)
            
            slots_available -= 1
            
            result.append([job_id ,deadline])
            
            result.sort(key=lambda x: x[1])
            
            
            for job in result:
                print(job[0] , end=" ")
                
            print()
            
if __name__ == '__main__':
    arr=[['a',2,200],
        ['b',1,129],
        ['c',3,40],
        ['d',1,25],
        ['e',1,15]]
        
    print("Following is maximum profit sequence of jobs ")
    
    printjobscheduling(arr)
            
            
#OUTPUT
#Following is maximum profit sequence of jobs 
"""c 
a c 
b a c """
