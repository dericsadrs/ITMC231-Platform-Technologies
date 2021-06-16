all: basic_ops.c

main: main.o
	gcc -o main basic_ops.c -lm
main.o: basic_ops.c
	gcc -c -o main.o basic_ops.c
test: main 
	./main > result.out
clean:
	rm -rf main *.o *.out
