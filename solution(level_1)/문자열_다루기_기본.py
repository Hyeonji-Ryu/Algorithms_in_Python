# 문제 설명

# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요.
# 예를 들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.

# 제한 사항

# s는 길이 1 이상, 길이 8 이하인 문자열입니다.

def solution(s):
    number=['1','2','3','4','5','6','7','8','9','0']

    if len(s)== 4 or len(s)== 6:

        for i in range(0, len(s)):
            if s[i] in number:
                answer = True
            else:
                answer = False
                break

    else:
        answer = False
        
    return answer
