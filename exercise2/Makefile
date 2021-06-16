#Author's Name San Andres Deric 
#Course and Year, 2ND BS-IT
#Honor Code which states the following: I have not given nor received any
#unathorized help in completing this exercise. I am also well aware of the policies
#stipulated in the AdNU student handbook.

main: main.o
	gcc -o main main.c -lm
main.0: main.c
	gcc -c -o main.o main.c
testc:main
	./main <exercise2.in> exercise2-c.out
testpy:main.py
	python3 main.py <exercise2.in> exercise2-py.out
clean:
	rm -rf main *.o*.out
