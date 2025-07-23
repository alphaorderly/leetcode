class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        st = []

        ans = 0

        for idx, ch in enumerate(s):
            if x > y:
                if st and st[-1] == 'a' and ch == 'b':
                    st.pop()
                    ans += x
                else:
                    st.append(ch)
            else:
                if st and st[-1] == 'b' and ch == 'a':
                    st.pop()
                    ans += y
                else:
                    st.append(ch)

        st2 = []

        for idx, ch in enumerate(st):
            if x <= y:
                if st2 and st2[-1] == 'a' and ch == 'b':
                    st2.pop()
                    ans += x
                else:
                    st2.append(ch)
            else:
                if st2 and st2[-1] == 'b' and ch == 'a':
                    st2.pop()
                    ans += y
                else:
                    st2.append(ch)

        return ans