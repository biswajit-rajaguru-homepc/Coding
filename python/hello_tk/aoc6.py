
def is_packet_start_marker(word):
    for index,c in enumerate(word):
        if index == len(word) - 1:
            return True
        if c in word[index+1:]:
            return False
    


print(is_packet_start_marker("Biswajt1234567891"))
    


# for part 2 subtitute 4 with 14

with open('puzzle_6_data', 'r') as f:
    data_stream = f.readline().strip()
    # print(data_stream)
    pos =0
    for c in data_stream:
        # print(c,end=" ")
        if len(data_stream) - pos < 14:
            print("There is no packet start marker in the data stream")
            exit(0)
        word = data_stream[pos:pos+14]
        if is_packet_start_marker(word):
            print(f"the data packet starts after {pos+14} bytes {word} ")
            break
        pos += 1
    
    
            
        
    
    