def solution(word, pages):
    answer = (0, 0)
    N = len(pages)
    word = word.lower()
    site = [''] * N
    external_link = [[] for _ in range(N)]
    basic_score = [0] * N
    link_score = [0] * N
    for i in range(len(pages)):
        # 소문자로 전체 변환
        page = pages[i].lower()
        # 웹페이지 링크 찾기
        meta_start = 0
        while True:
            meta_start = page.find('<meta property="og:url"', meta_start)
            if meta_start == -1: break
            meta_end = page.find('>', meta_start)
            link_idx = page.find('https://', meta_start)
            if link_idx == -1:
                meta_start = meta_end + 1
                continue
            link = page[link_idx:page.find('"/>', link_idx)]
            site[i] = link.strip()
            break
        # 외부 링크 찾기
        external_idx = 0
        while True:
            external_idx = page.find('<a href="', external_idx)
            if external_idx == -1:
                break
            external_idx += 9
            href = page[external_idx:page.find('"', external_idx)]
            external_link[i].append(href.strip())
        # 일치 단어 찾기
        word_start = 0
        while True:
            word_start = page.find(word, word_start)
            if word_start == -1:
                break
            word_end = word_start + len(word)
            if (ord(page[word_start-1]) < 97 or ord(page[word_start-1]) > 122) and (ord(page[word_end]) < 97 or ord(page[word_end]) > 122):
                basic_score[i] += 1
            word_start = word_end
    for i in range(len(external_link)):
        for el in external_link[i]:
            if not el in site: continue
            ei = site.index(el)
            link_score[ei] += basic_score[i] / len(external_link[i])

    for i in range(N):
        score = basic_score[i] + link_score[i]
        if answer[1] < score:
            answer = (i, score)
    return answer[0]


print(solution('blind', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print(solution('Muzi', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))
