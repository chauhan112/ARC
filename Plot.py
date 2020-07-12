import matplotlib.pyplot as plt 
from matplotlib import colors
class Plot:
    def __init__(self, task):
        self.task = task
        self.plot_task()
    def plot_one(self,ax, i,train_or_test,input_or_output):
        cmap = colors.ListedColormap(
            ['#000000', '#0074D9','#FF4136','#2ECC40','#FFDC00',
            '#AAAAAA', '#F012BE', '#FF851B', '#7FDBFF', '#870C25'])
        norm = colors.Normalize(vmin=0, vmax=9)
        
        input_matrix = self.task[train_or_test][i][input_or_output]
        ax.imshow(input_matrix, cmap=cmap, norm=norm)
        ax.grid(True,which='both',color='lightgrey', linewidth=0.5)    
        ax.set_yticks([x-0.5 for x in range(1+len(input_matrix))])
        ax.set_xticks([x-0.5 for x in range(1+len(input_matrix[0]))])     
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_title(train_or_test + ' '+input_or_output)
        
    def plot_task(self):
        #Plots the first train and test pairs of a specified task,
        #using same color scheme as the ARC app   
        num_train = len(self.task['train'])
        fig, axs = plt.subplots(2, num_train, figsize=(3*num_train,3*2))
        for i in range(num_train):     
            self.plot_one(axs[0,i],i,'train','input')
            self.plot_one(axs[1,i],i,'train','output')        
        plt.tight_layout()
        plt.show()        
            
        num_test = len(self.task['test'])
        fig, axs = plt.subplots(2, num_test, figsize=(3*num_test,3*2))
        if num_test==1: 
            self.plot_one(axs[0],0,'test','input')
            self.plot_one(axs[1],0,'test','output')     
        else:
            for i in range(num_test):      
                self.plot_one(axs[0,i],i,'test','input')
                self.plot_one(axs[1,i],i,'test','output')  
        plt.tight_layout()
        plt.show() 