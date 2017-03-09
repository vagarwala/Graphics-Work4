run: main.py
	python main.py

.PHONY: clean
clean:
	rm -f *.pyc *~ *.ppm *.png

.PHONY: all
all: clean run