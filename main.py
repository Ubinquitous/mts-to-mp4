import subprocess

def convert_mts_to_mp4(input_file, output_file):
    command = [
        'ffmpeg',
        '-i', input_file, 
        '-c:v', 'libx264', 
        '-crf', '18',     
        '-preset', 'slow',
        '-c:a', 'aac',    
        '-b:a', '192k',   
        '-strict', 'experimental', 
        output_file       
    ]
    
    try:
        subprocess.run(command, check=True)
        print("변환 완료")
    except subprocess.CalledProcessError as e:
        print("오류오류")

print("변환할 MTS 파일을 추가하고 이름을 입력하세요: ", end="")
input_file = input()
output_file = "result.mp4"
convert_mts_to_mp4(input_file, output_file)
