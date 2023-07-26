-- 예제 2: 각 팀에 대해, 최고 점수차로 이긴 게임의 
-- 상대팀 아이디, 게임이 열린 날짜와 경기장 아이디, 점수차 및 경기 점수를 검색하시오.
-- 최고 점수차로 이긴 게임이 2개 이상이면 모두 나열하시오.
-- 단, 경기 점수는 '이긴팀 점수: 진팀점수'로 표현하시오.
USE KLEAGUE;
WITH T AS (
    SELECT HOMETEAM_ID AS 이긴팀,
        AWAYTEAM_ID AS 진팀,
        SCHE_DATE AS 경기날짜,
        STADIUM_ID AS 경기장,
        (HOME_SCORE - AWAY_SCORE) AS 점수차,
        CONCAT(HOME_SCORE, ':', AWAY_SCORE) AS 경기점수
    FROM SCHEDULE
    WHERE (HOME_SCORE - AWAY_SCORE) > 0
    UNION
    SELECT AWAYTEAM_ID 이긴팀,
        HOMETEAM_ID 진팀,
        SCHE_DATE 경기날짜,
        STADIUM_ID 경기장,
        (AWAY_SCORE - HOME_SCORE) 점수차,
        CONCAT(AWAY_SCORE, ':', HOME_SCORE) 경기점수
    FROM SCHEDULE
    WHERE (AWAY_SCORE - HOME_SCORE) > 0
)
SELECT 이긴팀,
    진팀,
    경기날짜,
    경기장,
    점수차,
    경기점수
FROM T AS T1
WHERE 점수차 = (
        SELECT MAX(점수차)
        FROM T AS T2
        WHERE T1.이긴팀 = T2.이긴팀
        GROUP BY 이긴팀
    )
ORDER BY 이긴팀;