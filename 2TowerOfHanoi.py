def TOH(num,source,destination,aux):
    if num == 1:
        print(f"Move disk {num} from {source} to {destination}")
        return
    
    TOH(num-1,source,aux,destination)
    print(f"Move disk {num} from {source} to {destination}")
    TOH(num - 1,aux, destination, source)
    
num = 3
TOH(num,'A','C','B')