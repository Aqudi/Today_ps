-- 예제3: GK가 4인 이상 있는 팀의 팀명과 GK선수의 인원수,
-- 팀 전체 선수의 인원수를 검색하시오.
USE KLEAGUE;
SELECT TEAM_ID,
    TEAM_NAME,
    COUNT(*) AS 'gk 선수인원수',
    (
        SELECT COUNT(*)
        FROM PLAYER
        WHERE PLAYER.TEAM_ID = P.TEAM_ID
    ) AS 총인원수
FROM PLAYER P
    NATURAL JOIN TEAM
WHERE POSITION = 'GK'
GROUP BY P.TEAM_ID,
    POSITION
HAVING P.TEAM_ID IN (
        SELECT P2.TEAM_ID
        FROM PLAYER P2
        WHERE P2.POSITION = 'GK'
        GROUP BY P2.TEAM_ID,
            P2.POSITION
        HAVING COUNT(P2.POSITION) >= 4
    )
ORDER BY TEAM_ID;