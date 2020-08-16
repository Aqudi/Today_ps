-- 예제4 : 홈에서 진 적이 없는 팀을 검색하시오.
-- 단, 홈경기가 없던 팀은 제외하시오.
USE KLEAGUE;
WITH PLAYS AS (
    SELECT HOMETEAM_ID,
        (HOME_SCORE >= AWAY_SCORE) WIN_DRAW,
        (HOME_SCORE < AWAY_SCORE) LOSE,
        (HOME_SCORE - AWAY_SCORE) SCORE
    FROM SCHEDULE
    WHERE GUBUN = 'Y'
)
SELECT TEAM_ID,
    SUM(WIN_DRAW),
    SUM(LOSE) -- DISTINCT TEAM_ID, SUM(WIN_DRAW), SUM(LOSE)
FROM TEAM
    JOIN PLAYS ON TEAM_ID = HOMETEAM_ID
GROUP BY TEAM_ID
HAVING SUM(LOSE) = 0
ORDER BY TEAM_ID;
-- 풀이2
USE KLEAGUE;
WITH PLAY_TEAM AS (
    SELECT HOMETEAM_ID
    FROM SCHEDULE
    WHERE GUBUN = 'Y'
)
SELECT DISTINCT P.HOMETEAM_ID
FROM PLAY_TEAM AS P
WHERE P.HOMETEAM_ID NOT IN (
        SELECT DISTINCT S.HOMETEAM_ID
        FROM SCHEDULE AS S
        WHERE HOME_SCORE - AWAY_SCORE < 0
    );