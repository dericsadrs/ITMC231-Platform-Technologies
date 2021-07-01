vendor_id: vendor_id.exe
	.\vendor_id
brand_string: brand_string.c
	gcc brand_string.c -o brand_string
test: api.py
	python3 api.py < test.in | tee -a test.out
clean:
	rm - rf *.o *.out




