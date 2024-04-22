GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

--NOTES: We will need a pivot table between Coaches & Teams.

DROP TABLE IF EXISTS [dbo].Coaches
if not EXISTS(select * from sys.tables t join sys.schemas s on (t.schema_id = s.schema_id) where s.name = 'dbo' and t.name = 'Coaches')
BEGIN
CREATE TABLE [dbo].[Coaches](
		[CoachID] [int] IDENTITY(1,1) NOT NULL,
		[Name] [nvarchar](255) NOT NULL,
		[Description] [nvarchar](max) NULL,
		PRIMARY KEY (CoachID),
	) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY] --kinda redundant definition of where very large files go. If we had a custom file group it would matter but it's just going to the default location for now. Don't worry about this line in other words.
END
--we could do a drop table and then recreate the table here also... For now this will do though.

--ELSE
--BEGIN
--ALTER TABLE [dbo].[Coaches]
--	Add [examplecol] [int] not null
--END

GO