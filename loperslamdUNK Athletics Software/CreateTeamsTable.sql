GO

/****** Object:  Table [dbo].[Teams]    Script Date: 3/27/2024 1:42:08 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

DROP TABLE IF EXISTS [dbo].Teams
if not EXISTS(select * from sys.tables t join sys.schemas s on (t.schema_id = s.schema_id) where s.name = 'dbo' and t.name = 'Teams')
BEGIN
CREATE TABLE [dbo].[Teams](
		[TeamID] [int] IDENTITY(1,1) NOT NULL,
		[Name] [nvarchar](255) NOT NULL,
		[Description] [nvarchar](max) NULL,
		PRIMARY KEY (TeamID),
	) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY] --kinda redundant definition of where very large files go. If we had a custom file group it would matter but it's just going to the default location for now. Don't worry about this line in other words.
END
--we could do a drop table and then recreate the table here also... For now this will do though.

--ELSE
--BEGIN
--ALTER TABLE [dbo].[Teams]
--	Add [examplecol] [int] not null
--END

GO