CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      select distinct Salary as getNthHighestSalary from Employee group by Salary order by Salary desc limit 1 offset N      
  );
END
