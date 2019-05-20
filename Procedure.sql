/* One Procedure to Select records from a table and Print */
create or replace PACKAGE BODY package_example AS
PROCEDURE proc_example(args1 type1%TYPE,args2 type2%TYPE,output1 OUT SYS_REFCURSOR)
	IS
	BEGIN
			OPEN output1 FOR
            select *
            from  table1
             where
            roll_id=args1 and pin=args2
       
EXCEPTION
		  WHEN OTHERS THEN
		  ROLLBACK;
	END proc_example;
END  package_example;
