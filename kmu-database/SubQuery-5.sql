-- 예제5: 각 팀의 승리한 게임수, 무승부한 게임수, 패배한 게임수, 그리고 팀의 전체 게임수
-- 단, 점수가 없는 경기는 실제 진행되지 않았으므로, 게임수에서 제외하시오.
WITH PLAYS AS (
	SELECT HOMETEAM_ID TEAM_ID, (AWAY_SCORE - HOME_SCORE) AS SCORE,
		CASE
			WHEN (HOME_SCORE - AWAY_SCORE) > 0 THEN 'WIN'
			WHEN (HOME_SCORE - AWAY_SCORE) < 0 THEN 'LOSE'
			ELSE 'DRAW'
		END RESULT
    FROM SCHEDULE
    WHERE GUBUN = 'Y'
    UNION ALL
	SELECT AWAYTEAM_ID TEAM_ID, (AWAY_SCORE - HOME_SCORE) AS SCORE,
		CASE
			WHEN (AWAY_SCORE - HOME_SCORE) > 0 THEN 'WIN'
			WHEN (AWAY_SCORE - HOME_SCORE) < 0 THEN 'LOSE'
			ELSE 'DRAW'
		END RESULT
    FROM SCHEDULE
    WHERE GUBUN = 'Y'
)
SELECT TEAM_ID, COUNT(*),
		COUNT(CASE RESULT WHEN 'DRAW'	THEN RESULT		END) DRAW,
        COUNT(CASE RESULT WHEN 'WIN'	THEN RESULT 	END) WIN,
        COUNT(CASE RESULT WHEN 'LOSE' 	THEN RESULT 	END) LOSE
FROM PLAYS AS P
GROUP BY TEAM_ID;
