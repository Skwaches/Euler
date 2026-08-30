files=$(wildcard *.cpp)
BUILD=build


%: %.cpp $(BUILD)
	g++ -O3 $< -o $(BUILD)/$@
	./$(BUILD)/$@

$(BUILD):
	mkdir -p $(BUILD)

clean:
	rm -f $(BUILD)/$(QUE)
