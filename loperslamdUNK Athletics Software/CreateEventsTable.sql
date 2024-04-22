GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

DROP TABLE IF EXISTS [dbo].Events
if not EXISTS(select * from sys.tables t join sys.schemas s on (t.schema_id = s.schema_id) where s.name = 'dbo' and t.name = 'Events')
BEGIN
CREATE TABLE [dbo].[Events](
		[EventID] [int] IDENTITY(1,1) NOT NULL,
		[Name] [nvarchar](255) NOT NULL,
		[Date] [nvarchar](255) NOT NULL,
		TeamID INT,
		PRIMARY KEY (EventID),
		FOREIGN KEY (TeamID) REFERENCES dbo.teams(TeamID),
	) ON [PRIMARY]
END
GO