''' This is a Python script which is calling Procedure file of this repository 
and Prints the 3 outputs on screen'''
import cx_Oracle
    
def run_Proc():
	args1=708
	args2=54

	conn_str = u'username/pwd@hostname:portnumber/sid'
	conn = cx_Oracle.connect(conn_str)
	c = conn.cursor()
	output1 = c.var(cx_Oracle.CURSOR)
	output2 = c.var(cx_Oracle.CURSOR)
	output3 = c.var(cx_Oracle.CURSOR)
	c.callproc('package_example.proc_example',
      [args1, args2,output1,output2,output3])   
      
      
	for mc in output1.getvalue():
		print(mc[0],mc[1],mc[2],mc[3],mc[4],mc[5],mc[6],mc[7])
	
   
	conn.close()
	
	
run_Proc()
