from jamo import h2j, j2hcj, is_hangul_char

# https://jinh.kr/morse/ 한국어 모스 부호 변환 참고
MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.',     'F': '..-.', 'G': '--.',  'H': '....',
    'I': '..',    'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--',    'N': '-.',   'O': '---',  'P': '.--.',
    'Q': '--.-',  'R': '.-.',  'S': '...',  'T': '-',
    'U': '..-',   'V': '...-', 'W': '.--',  'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ' ': '/',
    'ㄱ': '.-',   'ㄴ': '-...', 'ㄷ': '-..', 'ㄹ': '.-..',
    'ㅁ': '--',   'ㅂ': '-.-',  'ㅅ': '...', 'ㅇ': '-.--',
    'ㅈ': '--.-', 'ㅊ': '---.', 'ㅋ': '.--', 'ㅌ': '..-..',
    'ㅍ': '.---', 'ㅎ': '----',
    'ㅏ': '.-',   'ㅑ': '-.-',  'ㅓ': '-..', 'ㅕ': '--.',
    'ㅗ': '---',  'ㅛ': '.--.', 'ㅜ': '..--','ㅠ': '-..-',
    'ㅡ': '...-', 'ㅣ': '-.-.'
}

def get_user_input():
    user_input = input("모스 부호로 변환할 문자열을 입력하세요: ")
    return user_input

def decompose_korean(text):
    decomposed_text = []
    for char in text:
        if is_hangul_char(char):
            decomposed_text.extend(j2hcj(h2j(char)))
        else:
            decomposed_text.append(char)
    return decomposed_text

def text_to_morse(text):
    morse_text = []
    unsupported_chars = []
    text = text.upper()
    decomposed_text = decompose_korean(text)
    for char in decomposed_text:
        morse_value = MORSE_CODE_DICT.get(char, None)
        if morse_value:
            morse_text.append(morse_value)
        else:
            unsupported_chars.append(char)
    if unsupported_chars:
        print(f"경고: 다음 문자는 모스 부호로 변환할 수 없습니다: {', '.join(unsupported_chars)}")
    return ' '.join(morse_text)

def print_morse(morse_code):
    print(f"\n모스 부호: {morse_code}\n")

def validate_input(text):
    if not text:
        print("입력된 문자열이 비어 있습니다. 다시 시도해주세요.")
        return False
    return True

def main():
    while True:
        user_input = get_user_input()
        if validate_input(user_input):
            morse_code = text_to_morse(user_input)
            print_morse(morse_code)

        retry = input("추가로 변환하려면 'y'를 입력하고, 종료하려면 아무 키나 누르세요: ").lower()
        if retry != 'y':
            print("프로그램을 종료합니다.")
            break

if __name__ == "__main__":
    main()
