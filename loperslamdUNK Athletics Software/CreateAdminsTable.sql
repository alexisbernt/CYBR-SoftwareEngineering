GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

DROP TABLE IF EXISTS [dbo].Admins
if not EXISTS(select * from sys.tables t join sys.schemas s on (t.schema_id = s.schema_id) where s.name = 'dbo' and t.name = 'Admins')
BEGIN
CREATE TABLE [dbo].[Admins](
		[Username] [nvarchar](255) NOT NULL,
		[Key] [nvarchar](255) NOT NULL,
		PRIMARY KEY (Username),
	) ON [PRIMARY]
END
GO