BUILD=build
FILES=$(wildcard *.cpp)
OUTPUTS=$(FILES:%.cpp=$(BUILD)/%)

.PHONY: $(Q)
$(Q): $(BUILD)/$(Q)

all: $(OUTPUTS)

$(BUILD):
	mkdir -p $(BUILD)

$(BUILD)/%: %.cpp $(BUILD)
	g++ -O3 $< -o $@

run: $(BUILD)/$(Q) 
	./$(BUILD)/$(Q)
	
clean: 
	rm -r $(BUILD)/$(Q)
