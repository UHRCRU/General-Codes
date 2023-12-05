/****** Script for SelectTopNRows command from SSMS  ******/
SELECT  [AppID]
      ,[Name]
      ,[Release date]
      ,[Estimated owners]
      ,[Peak CCU]
      ,[Required age]
      ,[Price]
      ,[DLC count]
      ,[Support email]
      ,[Positive]
      ,[Negative]
      ,[Achievements]
      ,[Recommendations]
      ,[Average playtime forever]
      ,[Average playtime two weeks]
      ,[Developers]
      ,[Publishers]
  FROM [SteamGames].[dbo].[games]
  
  
  
  select  distinct[AppID],
   HASHBYTES('MD5', [AppID]) as AppID_key 
  from [SteamGames].[dbo].[games]
  
  
  
  select distinct [Release date] FROM [SteamGames].[dbo].[games]
  order by [Release date]
  
Select 
CAST([Required age] as DECIMAL(32)) as REQUIRED_AGE

FROM [SteamGames].[dbo].[games]

  SELECT  
      [Positive]
      ,[Negative]
      ,[Achievements]
      ,[Recommendations]
      ,[Average playtime forever]
      ,[Average playtime two weeks]
       ,HASHBYTES('MD5', [AppID]) as AppID_key 
		,HASHBYTES('MD5', [Required age]) as Required_age_key
		,HASHBYTES('MD5', [Estimated owners]) as Estimated_owners_key
		,HASHBYTES('MD5', [Release date]) as Release_date_key
		,HASHBYTES('MD5', [Publishers]) as Publishers_key 
 FROM [SteamGames].[dbo].[games]
  
SELECT  
		[Required age], 
        HASHBYTES('MD5', [Required age]) as Required_age_key 
		INTO [SteamGames].[dbo].[Dim_RequiredAge]
FROM [SteamGames].[dbo].[games]

SELECT  
		distinct[Estimated owners],
		HASHBYTES('MD5', [Estimated owners]) as Estimated_owners_key
		--INTO [SteamGames].[dbo].[Dim_EstimatedOwners]
FROM [SteamGames].[dbo].[games]

SELECT  
		[Release date],
		HASHBYTES('MD5', [Release date]) as Release_date_key
		INTO [SteamGames].[dbo].[Dim_ReleaseDate]
FROM [SteamGames].[dbo].[games]

  SELECT  
		distinct[Publishers],
		HASHBYTES('MD5', [Publishers]) as Publishers_key 
		--INTO [SteamGames].[dbo].[Dim_Publishers]
FROM [SteamGames].[dbo].[games]

  Select 
 [average playtime forever]  as average_playtime_forever
  ,[Average playtime two weeks] as Average_playtime_two_weeks
       ,HASHBYTES('MD5', [AppID]) as AppID_key 
		,HASHBYTES('MD5', [Required age]) as Required_age_key
		,HASHBYTES('MD5', [Estimated owners]) as Estimated_owners_key
		,HASHBYTES('MD5', [Release date]) as Release_date_key
		,HASHBYTES('MD5', [Publishers]) as Publishers_key 
 INTO [SteamGames].[dbo].[GamesReadytoPBfacttable]
 FROM [SteamGames].[dbo].[games]