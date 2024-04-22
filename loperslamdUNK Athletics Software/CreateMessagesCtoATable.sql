GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

DROP TABLE IF EXISTS [dbo].MessagesCtoA
if not EXISTS(select * from sys.tables t join sys.schemas s on (t.schema_id = s.schema_id) where s.name = 'dbo' and t.name = 'MessagesCtoA')
BEGIN
CREATE TABLE [dbo].[MessagesCtoA](
		MessageID int IDENTITY(1,1) NOT NULL,
		[Subject] [nvarchar](255) NOT NULL,
		[Description] [nvarchar](255) NOT NULL,
		DateCreated DATETIME NOT NULL,
		CoachID INT,
		AthleteID INT,
		PRIMARY KEY (MessageID),
		FOREIGN KEY (CoachID) REFERENCES dbo.Coaches(CoachID),
		FOREIGN KEY (AthleteID) REFERENCES dbo.Athletes(AthleteID)
	) ON [PRIMARY] --kinda redundant definition of where very large files go. If we had a custom file group it would matter but it's just going to the default location for now. Don't worry about this line in other words.
END
--we could do a drop table and then recreate the table here also... For now this will do though.

--ELSE
--BEGIN
--ALTER TABLE [dbo].[Athletes]
--	Add [examplecol] [int] not null
--END

GO