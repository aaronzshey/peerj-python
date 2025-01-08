from Bio.Emboss.Applications import NeedleCommandline

# needle cli version
alignment_a_left = 0
alignment_b_left = 0
needle_cline = NeedleCommandline()
needle_cline.asequence = "000F.seq"
needle_cline.bsequence = "001F.seq"
needle_cline.gapopen = 10
needle_cline.gapextend= 0.5
needle_cline.outfile = "out.txt"

print(needle_cline)
stdout, stderr = needle_cline()
print(stdout + stderr)

def needle_align_to_get_boundaries(f1,f2):
    alignment_a_left = 0
    alignment_b_left = 0
    output_file_name = f1.split('.')[0] + f2.split('.')[0] + ".needle"
    
    needle_cline = NeedleCommandline()
    needle_cline.asequence = f1
    needle_cline.bsequence = f2
    needle_cline.gapopen = 10
    needle_cline.gapextend= 0.5
    needle_cline.outfile = output_file_name
    print(needle_cline)
    stdout, stderr = needle_cline()
    print(stdout + stderr)

    #open the needle alignment output file and get boundaries
    file = open(output_file_name)
    file_lines = file.readlines()
    file.close()

    for line in file_lines:
        print(line, end="")

    alignment_a_squence_positions = []
    alignment_b_squence_positions = []

    file = open(output_file_name)

    new_line1 = file.readline()
    new_line2 = file.readline()

    while len(new_line2):
        line_a = new_line1
        line_b = new_line2
        new_line2 = new_line2.strip()
        
        if (50*'|' in new_line2):

            line_b = file.readline()
      
            alignment_a_squence_line_str = line_a.strip()
            alignment_b_squence_line_str = line_b.strip()
            print("The beginning of excellent alignment is shown below.\n")
            
            alignment_a_squence_line_str_split = alignment_a_squence_line_str.split()
            print(alignment_a_squence_line_str_split[0].ljust(5,' '),\
                  alignment_a_squence_line_str_split[1],\
                  alignment_a_squence_line_str_split[2].rjust(6,' '),\
                  sep="")
            alignment_b_squence_line_str_split = alignment_b_squence_line_str.split()
            print(alignment_b_squence_line_str_split[0].ljust(5,' '),\
                  alignment_b_squence_line_str_split[1],\
                  alignment_b_squence_line_str_split[2].rjust(6,' '),\
                  sep="")
     
            print("\n")

            alignment_a_left = int(alignment_a_squence_line_str.split()[0])
            alignment_b_left = int(alignment_b_squence_line_str.split()[0])
            break
        else:
            new_line1 = new_line2         #notice the skill here, we must go step by step through the lines
            new_line2 = file.readline()
    file.close()

    return alignment_a_left, alignment_b_left


# print(needle_align_to_get_boundaries("000F.seq", "001F.seq"))