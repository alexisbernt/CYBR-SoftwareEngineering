GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

DROP TABLE IF EXISTS [dbo].CoachesTeams
if not EXISTS(select * from sys.tables t join sys.schemas s on (t.schema_id = s.schema_id) where s.name = 'dbo' and t.name = 'CoachesTeams')
BEGIN
CREATE TABLE [dbo].[CoachesTeams](
		[CoachID] int NOT NULL,
		[TeamID] int NOT NULL,
		PRIMARY KEY (CoachID, TeamID),
	) ON [PRIMARY]
END
GO