
'''import the necessary libraries'''
import datetime
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from functools import partial


'''setting the format of the date time'''
date_time=datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

class Main(QMainWindow):
    '''___________________the main class of the application_______________________'''

    def __init__(self):
        '''initialize the class'''
        super().__init__()

        '''the 10 dictionairy withe the key of name:__ and date:__ '''
        self.dict1={'name':'alpha','date':date_time}
        self.dict2={'name':'lawrence','date':date_time}
        self.dict3={'name':'peggy','date':date_time}
        self.dict4={'name':'hassan','date':date_time}
        self.dict5={'name':'sol','date':date_time}
        self.dict6={'name':'Alhakan','date':date_time}
        self.dict7={'name':'manikin','date':date_time}
        self.dict8={'name':'soline','date':date_time}
        self.dict9={'name':'katanorika','date':date_time}
        self.dict10={'name':'hanma','date':date_time}

        '''create a list containing the 10 dictionairy above'''
        self.dic_list=[self.dict1,self.dict2,self.dict3,self.dict4,self.dict5,self.dict6,self.dict7,self.dict8,self.dict9,self.dict10]

        '''get the length of the list'''
        self.length=len(self.dic_list)

        '''initialize the positioning attributes that will be use in the table'''
        self.index=0
        self.index=0
        self.first_colum=1
        self.second_colum=2
        self.button_colum=0
        self.row=0
        self.rowcount=1
        self.button_id=0

        '''the table heading titles'''
        self.tableheading=['Delete','Name','Date']
        
        '''call the interface method'''
        self.interface()
       
        


    def interface(self):
       '''Returns the interface of the current application'''
       self.gui=QFrame()
       self.gui.setStyleSheet('background-color:rgba(255,255,255,10)')
       
       '''create the table widget'''
       self.table=QTableWidget()
       self.table.setRowCount(self.length)
       self.table.setColumnCount(3)
       self.table.setHorizontalHeaderLabels(self.tableheading)
       self.table.setColumnWidth(0,230)
       self.table.setColumnWidth(2,500)
       self.table.setColumnWidth(1,505)
       vertical_scrollbar=self.table.verticalScrollBar()
       vertical_scrollbar.setStyleSheet('height:0;width:0; background-color:transparent')

       horizontal_scrollbar=self.table.horizontalScrollBar()
       horizontal_scrollbar.setStyleSheet('height:0;width:0; background-color:transparent') 
       self.table.setStyleSheet('''QTableWidget:item{background-color:rgba(255,255,255,150);COLOR:dodgerblue ;border-radius:0}
                                   QTableWidget:item:selected{background-color:skyblue;COLOR:red ;border-radius:0}
                                   QHeaderView:section{background-color:rgba(255,255,255,150);COLOR:yellow ;border-radius:0}''')
       

       
       
       for len in range(self.length):
            '''for loop that creates  and input data into the table using the len of the list as its range'''

            '''create qpushbutton name delete and style it'''
            self.delete=QPushButton('-')
            self.delete.setMaximumSize(80,80)
            self.delete.setCursor(Qt.CursorShape.PointingHandCursor)
            self.delete.setFont(QFont('ARIA',35,900,False))
            self.delete.setStyleSheet('''QPushButton{BACKGROUND-COLOR:rgba(255,255,255,100);border-radius:40 } QPushButton:Hover{BACKGROUND-COLOR:skyblue;border-radius:40; color: crimson} QPushButton:Pressed{BACKGROUND-COLOR:YELLOW;border-radius:40;color:skyblue }''' )
            self.delete.clicked.connect(partial( self.delete_row))

            ''''set the properties of the qtablewidget'''
            self.table.setRowHeight(self.button_colum,120)

            '''input the delete buttons and the data into the table'''
            self.table.setCellWidget(self.button_colum,0,self.delete)
            self.table.setItem(0,self.first_colum,QTableWidgetItem(self.dic_list[self.index]['name']))
            self.table.setItem(0,self.second_colum,QTableWidgetItem(self.dic_list[self.index]['date']))


            '''increment the position variables'''
            self.index=self.index+1
            self.first_colum=self.first_colum+3
            self.second_colum=self.second_colum+3
            self.button_colum=self.button_colum+1


       

       self.gui.showFullScreen()


       '''place the table into ths gui using the Qgridlayout'''
       self.frame_holder=QGridLayout(self.gui)
       self.frame_holder.addWidget(self.table)





    def delete_row(self):
        '''the delete function'''
        but=self.sender()
        if but:
            indexx=self.table.indexAt(but.pos())
            if indexx.isValid():
                index=indexx.row()
                if indexx !=0:
                    index=index
                    self.table.removeRow(index) 
                else:
                    self.table.removeRow(0) 
                      


        
        

        
            
            

    

    
''''run the application'''
if __name__=='__main__':
    app=QApplication([])
    main=Main()
    app.exec()