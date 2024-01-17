-- 예제 1: 각 팀의 최종 경기일을 검색하시오.
-- 단, 경기가 없던 팀은 제외하시오.
USE KLEAGUE;
SELECT TEAM.TEAM_ID,
    MAX(SCHE_DATE) 최종경기일
FROM TEAM
    JOIN SCHEDULE ON TEAM_ID IN (HOMETEAM_ID, AWAYTEAM_ID)
GROUP BY TEAM_ID
ORDER BY 1;