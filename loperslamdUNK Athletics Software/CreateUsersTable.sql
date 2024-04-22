GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

-- Note:
-- userRow = UsersTable(Signature=signature, Name=name, Email=email, Company=company, UserID=userID, InstallDateTime=ctime())

DROP TABLE IF EXISTS [dbo].Users
if not EXISTS(select * from sys.tables t join sys.schemas s on (t.schema_id = s.schema_id) where s.name = 'dbo' and t.name = 'Users')
BEGIN
CREATE TABLE [dbo].[Users](
		[Signature] int NOT NULL,
		UserID int IDENTITY(1,1) NOT NULL,
		[Name] [nvarchar](255) NOT NULL,
		Email [nvarchar](255) NOT NULL,
		Company [nvarchar](255) NOT NULL,
		InstallDateTime DATETIME NOT NULL,
		-- PRIMARY KEY ([Signature]), -- this is what they use in their made_db.py file... Not sure why they don't use a foreign key.
		PRIMARY KEY (UserID),
		FOREIGN KEY ([Signature]) REFERENCES dbo.Signatures(PrimaryKey)
	) ON [PRIMARY]
END
GO