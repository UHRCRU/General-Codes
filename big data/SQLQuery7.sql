/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [average_playtime_forever]
      ,[Average_playtime_two_weeks]
      ,[AppID_key]
      ,[Required_age_key]
      ,[Estimated_owners_key]
      ,[Release_date_key]
      ,[Publishers_key]
  FROM [SteamGames].[dbo].[GamesReadytoPBfacttable]