set serveroutput on;



DECLARE
    v_teste VARCHAR2 (30) := 'Hello, World!';
BEGIN
    DBMS_OUTPUT.enable;
    DBMS_OUTPUT.PUT_LINE(v_teste);
END;

declare
  message varchar2(20) := 'Hello World';
begin
  dbms_output.enable;
  dbms_output.put_line(message);
end ;