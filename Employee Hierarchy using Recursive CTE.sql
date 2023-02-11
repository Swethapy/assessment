Declare @EmpID Int
Set @EmpID = 7369;

With CTE
As
(
	-- Anchor member
	Select 
		EMPNO, 
		ENAME, 
		MGR 
	From Emp 
	Where EMPNO = @EmpID

	Union All

	-- Recursive member
	Select 
		E.EMPNO, 
		E.ENAME, 
		E.MGR
	From EMP E
	Inner Join CTE C
	On E.EMPNO = C.MGR
)
Select 
	E.EMPNO, 
	E.ENAME, 
	ISNULL(M.ENAME, 'CEO') As Manager
From CTE E
Left Join CTE M
On E.MGR = M.EMPNO;
