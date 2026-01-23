# Roblox Client FFlag Intel Report (350 Days)

- Last Run: 2026-01-23 05:24:48 PM PST
- Flags Added: 216
- Flags Changed: 814
- Flags Removed: 123

## Summary
| Category | Added | Changed | Removed | Total |
|---|---|---|---|---|
| Graphics | 6 | 0 | 3 | 9 |
| Physics | 7 | 1 | 4 | 12 |
| Network | 8 | 0 | 5 | 13 |
| Camera/UI | 19 | 1 | 11 | 31 |
| Security | 0 | 0 | 0 | 0 |
| World | 0 | 0 | 0 | 0 |
| Input | 2 | 0 | 1 | 3 |
| Hit | 0 | 0 | 0 | 0 |
| Interpolation | 0 | 0 | 0 | 0 |
| Body | 5 | 0 | 3 | 8 |
| Other | 169 | 812 | 96 | 1077 |

## History Summary

- Total Historical Added: 216
- Total Historical Changed: 814
- Total Historical Removed: 123
- Note: Limited history available.

## ba988ac9d - 2026-01-22 21:21:24 -0600 - 01/22/2026 21:21:24
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from af33f847885d3193956d71653efcfeb586693de7 to e98e685368b6d92186fc9e96d9f2b192243af944 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/23/2026 03:18:31 to 01/23/2026 03:20:11 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from af33f847885d3193956d71653efcfeb586693de7 to e98e685368b6d92186fc9e96d9f2b192243af944 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/23/2026 03:18:31 to 01/23/2026 03:20:11 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
- FStringSystrayExperimentBucketSettings2 changed from v4-15-29 to "" | Mechanism: Controls settings for user interface experiments in the system tray. | Purpose: Improves user experience by testing new interface features.
Removed in Other:
- FStringSystrayExperimentBucketSettings2_Staged removed (was "";SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-23T01:58:26) | Mechanism: Adjusts settings for the experimental system tray features. | Purpose: Optimizes the testing of new features, improving user experience during trials.

## 26f782fdf - 2026-01-22 21:19:08 -0600 - 01/22/2026 21:19:08
Changed in Other:
- DFFlagStreamingHandleInvalidValues changed from True to False | Mechanism: Implements checks to manage unexpected or invalid data during streaming. | Purpose: Enhances game stability and reduces errors for players during gameplay.
- DFStringFlagRepoGitHashDynamicString changed from 578853f35e37d4459eef882419b16cb4ca097554 to af33f847885d3193956d71653efcfeb586693de7 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/23/2026 02:52:38 to 01/23/2026 03:18:31 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 578853f35e37d4459eef882419b16cb4ca097554 to af33f847885d3193956d71653efcfeb586693de7 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/23/2026 02:52:38 to 01/23/2026 03:18:31 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 3a1efc416 - 2026-01-22 20:54:28 -0600 - 01/22/2026 20:54:28
Changed in Other:
- DFIntDataModelPatcherLoadRetry changed from 10 to 3 | Mechanism: Retries loading the data model if it fails initially. | Purpose: Improves the reliability of loading game data, reducing errors for players.
- DFStringFlagRepoGitHashDynamicString changed from ff77eeac1422169fe55107400f96748b81d619eb to 578853f35e37d4459eef882419b16cb4ca097554 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/23/2026 02:05:04 to 01/23/2026 02:52:38 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from ff77eeac1422169fe55107400f96748b81d619eb to 578853f35e37d4459eef882419b16cb4ca097554 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/23/2026 02:05:04 to 01/23/2026 02:52:38 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- DFIntDataModelPatcherLoadRetry_Staged removed (was 3;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-23T01:21:21) | Mechanism: Implements retry logic for loading data models when initial attempts fail. | Purpose: Increases the chances of successfully loading games, reducing errors for players.

## acec5c654 - 2026-01-22 20:07:54 -0600 - 01/22/2026 20:07:53
Added in Other:
- FStringSystrayExperimentBucketSettings2_Staged = "";SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-23T01:58:26 | Mechanism: Adjusts settings for the experimental system tray features. | Purpose: Optimizes the testing of new features, improving user experience during trials.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 74d7f9b165db11535f87113207053a16605775f3 to ff77eeac1422169fe55107400f96748b81d619eb | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/23/2026 01:49:09 to 01/23/2026 02:05:04 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 74d7f9b165db11535f87113207053a16605775f3 to ff77eeac1422169fe55107400f96748b81d619eb | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/23/2026 01:49:09 to 01/23/2026 02:05:04 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 146b68704 - 2026-01-22 19:50:02 -0600 - 01/22/2026 19:50:02
Added in Other:
- DFFlagHttpCacheAllowEmptyUrlInAssetCacheHeaders = True | Mechanism: Enables caching for assets even if the URL is empty in headers. | Purpose: Improves asset loading efficiency and reduces errors in asset retrieval.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 1c5f197a4e7d3c86a595f89c69da558254d95cb0 to 74d7f9b165db11535f87113207053a16605775f3 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/23/2026 01:22:37 to 01/23/2026 01:49:09 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 1c5f197a4e7d3c86a595f89c69da558254d95cb0 to 74d7f9b165db11535f87113207053a16605775f3 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/23/2026 01:22:37 to 01/23/2026 01:49:09 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- DFFlagHttpCacheAllowEmptyUrlInAssetCacheHeaders_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-23T00:44:28) | Mechanism: Enables caching of assets even if the URL is empty. | Purpose: Improves performance by allowing more flexible asset management.

## b98f17b9c - 2026-01-22 19:23:32 -0600 - 01/22/2026 19:23:32
Added in Other:
- DFIntDataModelPatcherLoadRetry_Staged = 3;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-23T01:21:21 | Mechanism: Implements retry logic for loading data models when initial attempts fail. | Purpose: Increases the chances of successfully loading games, reducing errors for players.
Changed in Other:
- DFIntRemoteAllowListDisallowedNameHundredthsPercentage changed from 1000 to 50 | Mechanism: Sets a limit on certain remote function names. | Purpose: Increases security by preventing misuse of specific function names.
- DFStringFlagRepoGitHashDynamicString changed from cda64966e54237be33ab5dbc842000920a91c65a to 1c5f197a4e7d3c86a595f89c69da558254d95cb0 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/23/2026 00:56:31 to 01/23/2026 01:22:37 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from cda64966e54237be33ab5dbc842000920a91c65a to 1c5f197a4e7d3c86a595f89c69da558254d95cb0 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/23/2026 00:56:31 to 01/23/2026 01:22:37 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- DFIntRemoteAllowListDisallowedNameHundredthsPercentage_Staged removed (was 50;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-23T00:18:57) | Mechanism: Sets a percentage limit on certain disallowed names in remote functions. | Purpose: Helps maintain a safe and appropriate naming environment for players.

## b28ff4874 - 2026-01-22 18:57:01 -0600 - 01/22/2026 18:57:01
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 5dffc9c73efc3c610d0d772cf3379d1e0fee961c to cda64966e54237be33ab5dbc842000920a91c65a | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/23/2026 00:46:34 to 01/23/2026 00:56:31 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 5dffc9c73efc3c610d0d772cf3379d1e0fee961c to cda64966e54237be33ab5dbc842000920a91c65a | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/23/2026 00:46:34 to 01/23/2026 00:56:31 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## c789b6391 - 2026-01-22 18:48:07 -0600 - 01/22/2026 18:48:07
Changed in Other:
- DFIntBatchLogEventSenderLinearLoggingUniverseSamplingPerMille changed from 2 to 10 | Mechanism: Adjusts how event logging is sampled and sent for performance tracking. | Purpose: Provides better insights into game performance, helping developers optimize experiences for players.
- DFStringFlagRepoGitHashDynamicString changed from 8762c93f27696ba46a18aef37cabc5b2513db346 to 5dffc9c73efc3c610d0d772cf3379d1e0fee961c | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/23/2026 00:45:16 to 01/23/2026 00:46:34 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 8762c93f27696ba46a18aef37cabc5b2513db346 to 5dffc9c73efc3c610d0d772cf3379d1e0fee961c | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/23/2026 00:45:16 to 01/23/2026 00:46:34 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- DFIntBatchLogEventSenderLinearLoggingUniverseSamplingPerMille_Staged removed (was 10;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;false;1486362466;2026-01-22T23:41:18) | Mechanism: Adjusts how event logging is sampled for performance tracking. | Purpose: Improves the accuracy of performance data to enhance game stability.

## 8277b6159 - 2026-01-22 18:45:51 -0600 - 01/22/2026 18:45:51
Added in Other:
- DFFlagHttpCacheAllowEmptyUrlInAssetCacheHeaders_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-23T00:44:28 | Mechanism: Enables caching of assets even if the URL is empty. | Purpose: Improves performance by allowing more flexible asset management.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 308df762f5e6af2edf3504186d6081553a17f067 to 8762c93f27696ba46a18aef37cabc5b2513db346 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/23/2026 00:27:18 to 01/23/2026 00:45:16 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 308df762f5e6af2edf3504186d6081553a17f067 to 8762c93f27696ba46a18aef37cabc5b2513db346 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/23/2026 00:27:18 to 01/23/2026 00:45:16 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 654f9f90b - 2026-01-22 18:28:05 -0600 - 01/22/2026 18:28:05
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 307307b4db9bf514766185970e5c5b55e9235565 to 308df762f5e6af2edf3504186d6081553a17f067 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/23/2026 00:19:53 to 01/23/2026 00:27:18 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FFlagBirthdayPickerCenteringFix changed from True to False | Mechanism: Fixes the alignment of the birthday picker interface to be centered properly. | Purpose: Makes it easier for players to select their birthdays, improving user interface usability.
- FStringFlagRepoGitHashFastString changed from 307307b4db9bf514766185970e5c5b55e9235565 to 308df762f5e6af2edf3504186d6081553a17f067 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/23/2026 00:19:53 to 01/23/2026 00:27:18 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagBirthdayPickerCenteringFix_Staged removed (was false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;186514938;2026-01-22T23:21:05) | Mechanism: Adjusts the alignment of the birthday picker interface. | Purpose: Ensures the birthday picker looks centered and visually appealing for users.
- FFlagWrapDeformerUsesFMD3_Staged removed (was true;SteadyState;10;30;Revert;2026-01-22T23:52:58) | Mechanism: Implements a new deformation system for 3D models. | Purpose: Improves the visual quality of character animations and movements.

## 4d5688df4 - 2026-01-22 18:21:25 -0600 - 01/22/2026 18:21:24
Added in Other:
- DFIntRemoteAllowListDisallowedNameHundredthsPercentage_Staged = 50;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-23T00:18:57 | Mechanism: Sets a percentage limit on certain disallowed names in remote functions. | Purpose: Helps maintain a safe and appropriate naming environment for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from c071308ad106bc1196e0a59829462917eec81ecf to 307307b4db9bf514766185970e5c5b55e9235565 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/23/2026 00:17:16 to 01/23/2026 00:19:53 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from c071308ad106bc1196e0a59829462917eec81ecf to 307307b4db9bf514766185970e5c5b55e9235565 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/23/2026 00:17:16 to 01/23/2026 00:19:53 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 494af74f4 - 2026-01-22 18:19:08 -0600 - 01/22/2026 18:19:08
Added in Other:
- FFlagAppChatExcludeSyntheticPreviewFromMessages = True | Mechanism: Excludes synthetic message previews from chat logs. | Purpose: Improves chat clarity by removing unnecessary preview messages.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 7fc5cf31d7ddd7e1fc05ae6e2d398ec319fa382a to c071308ad106bc1196e0a59829462917eec81ecf | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/23/2026 00:13:11 to 01/23/2026 00:17:16 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 7fc5cf31d7ddd7e1fc05ae6e2d398ec319fa382a to c071308ad106bc1196e0a59829462917eec81ecf | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/23/2026 00:13:11 to 01/23/2026 00:17:16 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagAppChatExcludeSyntheticPreviewFromMessages_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T23:11:37) | Mechanism: Prevents synthetic message previews from appearing in chat. | Purpose: Improves chat clarity by showing only real messages.

## 6a430d62a - 2026-01-22 18:14:37 -0600 - 01/22/2026 18:14:37
Added in Other:
- DFFlagDataStoreEnableStartupThrottler = True | Mechanism: Limits the number of data store requests at startup to prevent overload. | Purpose: Ensures smoother game loading and better performance for players.
- FFlagEnablePlaceVersionHistory_IXP = 1;Studio.Collaboration.PlaceVersionHistory;Studio.Collaboration.PlaceVersionHistory;1318321993;flagbank | Mechanism: Enables tracking of different versions of game places. | Purpose: Allows developers to revert to previous versions of their games, improving development flexibility.
- FFlagGroupOSAGetConversationParticipants2 = True | Mechanism: Updates the method for retrieving participants in group conversations. | Purpose: Enhances communication features within groups for players.
Added in Physics:
- FFlagLuauSolverAgnosticPropType = True | Mechanism: Improves type checking in Luau scripts, making it more flexible. | Purpose: Helps developers write better scripts, leading to fewer bugs and a more stable game experience.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 7ca40999c6c1f2aeea61cbb796436610afce110c to 7fc5cf31d7ddd7e1fc05ae6e2d398ec319fa382a | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/23/2026 00:06:40 to 01/23/2026 00:13:11 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 7ca40999c6c1f2aeea61cbb796436610afce110c to 7fc5cf31d7ddd7e1fc05ae6e2d398ec319fa382a | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/23/2026 00:06:40 to 01/23/2026 00:13:11 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- DFFlagDataStoreEnableStartupThrottler_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;false;552871564;2026-01-22T23:10:10) | Mechanism: Implements a throttling system for data store access at startup. | Purpose: Improves game loading times and stability by managing data requests more efficiently.
- FFlagGroupOSAGetConversationParticipants2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T23:07:51) | Mechanism: Updates the way the system retrieves participants in group conversations. | Purpose: Provides players with more accurate and timely information about who is in a conversation.
Removed in Physics:
- FFlagLuauSolverAgnosticPropType_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T23:06:59) | Mechanism: Enables a more flexible property type system in Luau scripting. | Purpose: Allows developers to write more versatile scripts, enhancing game functionality.

## 96041b6f8 - 2026-01-22 18:07:47 -0600 - 01/22/2026 18:07:47
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 938a10e4777bd2fb7953f1fe566ae6976ad3b933 to 7ca40999c6c1f2aeea61cbb796436610afce110c | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/23/2026 00:01:24 to 01/23/2026 00:06:40 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 938a10e4777bd2fb7953f1fe566ae6976ad3b933 to 7ca40999c6c1f2aeea61cbb796436610afce110c | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/23/2026 00:01:24 to 01/23/2026 00:06:40 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 6f274875e - 2026-01-22 18:03:16 -0600 - 01/22/2026 18:03:16
Added in Other:
- FFlagAppChatGroupOsaPreventBlankDialog = True | Mechanism: Prevents empty chat dialogs from appearing in group chats. | Purpose: Enhances user experience by ensuring chat dialogs are meaningful and informative.
- FFlagAppChatSuppressGroupOSAContextCard = True | Mechanism: Prevents certain chat context cards from appearing in group chats. | Purpose: Reduces clutter in chat, making conversations clearer for players.
- FFlagIASModifierKeys = True | Mechanism: Enables the use of modifier keys for in-game actions. | Purpose: Allows players to perform advanced actions using keyboard shortcuts.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from bdc10fb2d39458c266ce55d7fc81865760084bd9 to 938a10e4777bd2fb7953f1fe566ae6976ad3b933 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 23:57:06 to 01/23/2026 00:01:24 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from bdc10fb2d39458c266ce55d7fc81865760084bd9 to 938a10e4777bd2fb7953f1fe566ae6976ad3b933 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 23:57:06 to 01/23/2026 00:01:24 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagAppChatGroupOsaPreventBlankDialog_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T22:58:23) | Mechanism: Prevents empty chat dialogs in group chats. | Purpose: Enhances communication by ensuring players can't send blank messages in group chats.
- FFlagAppChatSuppressGroupOSAContextCard_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T22:55:37) | Mechanism: Suppresses certain context cards in group chats within the app. | Purpose: Reduces distractions in group chats, allowing for smoother communication among players.
- FFlagIASModifierKeys_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T22:57:56) | Mechanism: Enables specific key combinations for input actions. | Purpose: Allows players to use custom key shortcuts for better control.

## 1c0942811 - 2026-01-22 17:58:47 -0600 - 01/22/2026 17:58:47
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from c025de0c75c9207104935c19af37d0a85cbc888f to bdc10fb2d39458c266ce55d7fc81865760084bd9 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 23:53:53 to 01/22/2026 23:57:06 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from c025de0c75c9207104935c19af37d0a85cbc888f to bdc10fb2d39458c266ce55d7fc81865760084bd9 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 23:53:53 to 01/22/2026 23:57:06 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 0fc331b7d - 2026-01-22 17:56:33 -0600 - 01/22/2026 17:56:32
Added in Other:
- FFlagWrapDeformerUsesFMD3_Staged = true;SteadyState;10;30;Revert;2026-01-22T23:52:58 | Mechanism: Implements a new deformation system for 3D models. | Purpose: Improves the visual quality of character animations and movements.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from f255a691cab117734e778987671cff04bd3e5340 to c025de0c75c9207104935c19af37d0a85cbc888f | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 23:53:27 to 01/22/2026 23:53:53 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from f255a691cab117734e778987671cff04bd3e5340 to c025de0c75c9207104935c19af37d0a85cbc888f | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 23:53:27 to 01/22/2026 23:53:53 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 6bfd0d418 - 2026-01-22 17:54:17 -0600 - 01/22/2026 17:54:16
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from ce1b3cb6984b437e7a71c3e88f6c735f6613e490 to f255a691cab117734e778987671cff04bd3e5340 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 23:42:05 to 01/22/2026 23:53:27 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from ce1b3cb6984b437e7a71c3e88f6c735f6613e490 to f255a691cab117734e778987671cff04bd3e5340 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 23:42:05 to 01/22/2026 23:53:27 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 227a066ed - 2026-01-22 17:43:02 -0600 - 01/22/2026 17:43:01
Added in Other:
- DFIntBatchLogEventSenderLinearLoggingUniverseSamplingPerMille_Staged = 10;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;false;1486362466;2026-01-22T23:41:18 | Mechanism: Adjusts how event logging is sampled for performance tracking. | Purpose: Improves the accuracy of performance data to enhance game stability.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 86f9238b3adb131e65ce5e41a5b3b8a52487d06d to ce1b3cb6984b437e7a71c3e88f6c735f6613e490 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 23:27:02 to 01/22/2026 23:42:05 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 86f9238b3adb131e65ce5e41a5b3b8a52487d06d to ce1b3cb6984b437e7a71c3e88f6c735f6613e490 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 23:27:02 to 01/22/2026 23:42:05 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## f9120b990 - 2026-01-22 17:29:40 -0600 - 01/22/2026 17:29:40
Added in Other:
- FFlagAppChatGroupOsaAnalytics3 = True | Mechanism: Integrates advanced analytics for group chat features to gather usage data. | Purpose: Helps improve group chat functionality based on how players use it, leading to better communication tools.
Added in Camera/UI:
- FFlagLoadStoredInputAudioDeviceEarlier = True | Mechanism: Loads the player's audio device settings sooner during game startup. | Purpose: Players can hear game sounds immediately without delay.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 2231dd9aa03e5136bca31fbe30045bf78fe478c3 to 86f9238b3adb131e65ce5e41a5b3b8a52487d06d | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 23:22:11 to 01/22/2026 23:27:02 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 2231dd9aa03e5136bca31fbe30045bf78fe478c3 to 86f9238b3adb131e65ce5e41a5b3b8a52487d06d | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 23:22:11 to 01/22/2026 23:27:02 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagAppChatGroupOsaAnalytics3_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T22:21:53) | Mechanism: Enhances analytics tracking for group chat features. | Purpose: Provides better insights into group chat usage, improving future updates and features.
Removed in Camera/UI:
- FFlagLoadStoredInputAudioDeviceEarlier_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T22:21:20) | Mechanism: Loads the player's audio device settings sooner during startup. | Purpose: Ensures audio settings are ready faster, enhancing the audio experience for players.

## c534e1fc7 - 2026-01-22 17:22:56 -0600 - 01/22/2026 17:22:56
Added in Other:
- FFlagBirthdayPickerCenteringFix_Staged = false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;186514938;2026-01-22T23:21:05 | Mechanism: Adjusts the alignment of the birthday picker interface. | Purpose: Ensures the birthday picker looks centered and visually appealing for users.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 9bd0dd3b10df2edea93336d6d717d8093c401ffa to 2231dd9aa03e5136bca31fbe30045bf78fe478c3 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 23:17:37 to 01/22/2026 23:22:11 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 9bd0dd3b10df2edea93336d6d717d8093c401ffa to 2231dd9aa03e5136bca31fbe30045bf78fe478c3 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 23:17:37 to 01/22/2026 23:22:11 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## e0b2c4610 - 2026-01-22 17:18:24 -0600 - 01/22/2026 17:18:23
Added in Other:
- FFlagAppChatGroupOsaNavigateBeforeRecordDecline = True | Mechanism: Modifies the chat interface to allow navigation before declining a group invite. | Purpose: Enhances user experience by letting players explore group details before making a decision.
- FFlagEventIngestTreatAcceptedAsSuccess = True | Mechanism: Changes how events are processed to treat accepted events as successful. | Purpose: Enhances the reliability of event handling in games.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 70b30d985d605492ec83d9ce3bc65cf0b6994e3b to 9bd0dd3b10df2edea93336d6d717d8093c401ffa | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 23:13:35 to 01/22/2026 23:17:37 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 70b30d985d605492ec83d9ce3bc65cf0b6994e3b to 9bd0dd3b10df2edea93336d6d717d8093c401ffa | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 23:13:35 to 01/22/2026 23:17:37 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagAppChatGroupOsaNavigateBeforeRecordDecline_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T22:12:10) | Mechanism: Modifies navigation flow in the chat app before declining a recording. | Purpose: Streamlines user experience when managing chat recordings.
- FFlagEventIngestTreatAcceptedAsSuccess_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T22:12:55) | Mechanism: Changes how event responses are processed to recognize accepted events as successful. | Purpose: Enhances event handling, making it clearer when actions are completed successfully.

## 075f10925 - 2026-01-22 17:16:04 -0600 - 01/22/2026 17:16:04
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from dbb38ac86f2e2c7d956170f4d153e3ed98a1e2f1 to 70b30d985d605492ec83d9ce3bc65cf0b6994e3b | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 23:12:25 to 01/22/2026 23:13:35 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from dbb38ac86f2e2c7d956170f4d153e3ed98a1e2f1 to 70b30d985d605492ec83d9ce3bc65cf0b6994e3b | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 23:12:25 to 01/22/2026 23:13:35 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 11b32874d - 2026-01-22 17:13:47 -0600 - 01/22/2026 17:13:46
Added in Other:
- DFFlagDataStoreEnableStartupThrottler_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;false;552871564;2026-01-22T23:10:10 | Mechanism: Implements a throttling system for data store access at startup. | Purpose: Improves game loading times and stability by managing data requests more efficiently.
- FFlagAppChatEnableGroupOSA3 = True | Mechanism: Activates a new chat feature for group interactions in the app. | Purpose: Allows players to communicate more effectively within their groups.
- FFlagAppChatExcludeSyntheticPreviewFromMessages_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T23:11:37 | Mechanism: Prevents synthetic message previews from appearing in chat. | Purpose: Improves chat clarity by showing only real messages.
- FFlagAppChatNavigateBackIfOSAUnacknowledged = True | Mechanism: Allows users to navigate back in chat if a message is not acknowledged. | Purpose: Improves user experience by making it easier to manage chat conversations.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 11c60ef45999ba03b6a6ad0943230b924043d74e to dbb38ac86f2e2c7d956170f4d153e3ed98a1e2f1 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 23:08:56 to 01/22/2026 23:12:25 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 11c60ef45999ba03b6a6ad0943230b924043d74e to dbb38ac86f2e2c7d956170f4d153e3ed98a1e2f1 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 23:08:56 to 01/22/2026 23:12:25 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagAppChatEnableGroupOSA3_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T22:08:16) | Mechanism: Activates a new chat system for group interactions. | Purpose: Enhances communication among group members, making it easier to collaborate in games.
- FFlagAppChatNavigateBackIfOSAUnacknowledged_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T22:09:42) | Mechanism: Allows users to navigate back in chat if the app's on-screen actions are not acknowledged. | Purpose: Improves user experience by letting players easily return to previous chat messages.

## 5250f58f4 - 2026-01-22 17:11:31 -0600 - 01/22/2026 17:11:30
Added in Other:
- FFlagGroupOSAGetConversationParticipants2_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T23:07:51 | Mechanism: Updates the way the system retrieves participants in group conversations. | Purpose: Provides players with more accurate and timely information about who is in a conversation.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 8abc586415aea533dc44db178cd2490155926655 to 11c60ef45999ba03b6a6ad0943230b924043d74e | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 23:07:51 to 01/22/2026 23:08:56 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 8abc586415aea533dc44db178cd2490155926655 to 11c60ef45999ba03b6a6ad0943230b924043d74e | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 23:07:51 to 01/22/2026 23:08:56 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 637cf73d7 - 2026-01-22 17:09:13 -0600 - 01/22/2026 17:09:13
Added in Physics:
- FFlagLuauSolverAgnosticPropType_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T23:06:59 | Mechanism: Enables a more flexible property type system in Luau scripting. | Purpose: Allows developers to write more versatile scripts, enhancing game functionality.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 8aba90634c6d397fc3ebdc42f81f2528c42144ec to 8abc586415aea533dc44db178cd2490155926655 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 23:05:50 to 01/22/2026 23:07:51 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 8aba90634c6d397fc3ebdc42f81f2528c42144ec to 8abc586415aea533dc44db178cd2490155926655 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 23:05:50 to 01/22/2026 23:07:51 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 02913afdf - 2026-01-22 17:06:56 -0600 - 01/22/2026 17:06:56
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from adf489a7c2e4ff88064d744efdc64c20c57360f0 to 8aba90634c6d397fc3ebdc42f81f2528c42144ec | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 23:03:42 to 01/22/2026 23:05:50 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from adf489a7c2e4ff88064d744efdc64c20c57360f0 to 8aba90634c6d397fc3ebdc42f81f2528c42144ec | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 23:03:42 to 01/22/2026 23:05:50 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 42265e2a9 - 2026-01-22 17:04:40 -0600 - 01/22/2026 17:04:40
Added in Other:
- DFFlagDataStoreEnableStartupThrottler_UniverseFilter = true;4800235170 | Mechanism: Limits the number of data store requests at startup based on the universe. | Purpose: Improves game loading times and stability by preventing overload on data services.
Changed in Other:
- DFFlagDataStoreEnableModernRequestCounters_UniverseFilter changed from true;3666294218;9343843562 to true;3666294218;9343843562;4800235170 | Mechanism: Implements modern counters for data store requests with universe filtering. | Purpose: Improves data management and efficiency for game developers.
- DFFlagDataStoreEnableModernRequestThrottling_UniverseFilter changed from true;3666294218;9343843562 to true;3666294218;9343843562;4800235170 | Mechanism: Implements a new system to manage how often data requests are made. | Purpose: Improves game performance by preventing overloads when accessing player data.
- DFStringFlagRepoGitHashDynamicString changed from cd2eb245147b98eefc0fc70fcdda6ecacc4414af to adf489a7c2e4ff88064d744efdc64c20c57360f0 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 23:00:16 to 01/22/2026 23:03:42 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from cd2eb245147b98eefc0fc70fcdda6ecacc4414af to adf489a7c2e4ff88064d744efdc64c20c57360f0 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 23:00:16 to 01/22/2026 23:03:42 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 0b0e019f7 - 2026-01-22 17:02:23 -0600 - 01/22/2026 17:02:22
Added in Other:
- FFlagAppChatGroupOsaPreventBlankDialog_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T22:58:23 | Mechanism: Prevents empty chat dialogs in group chats. | Purpose: Enhances communication by ensuring players can't send blank messages in group chats.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 36ceb6399c8f5bff235c3ccad3777870bdaec352 to cd2eb245147b98eefc0fc70fcdda6ecacc4414af | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 22:59:18 to 01/22/2026 23:00:16 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 36ceb6399c8f5bff235c3ccad3777870bdaec352 to cd2eb245147b98eefc0fc70fcdda6ecacc4414af | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 22:59:18 to 01/22/2026 23:00:16 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 53cffd93b - 2026-01-22 17:00:02 -0600 - 01/22/2026 17:00:02
Added in Other:
- FFlagIASModifierKeys_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T22:57:56 | Mechanism: Enables specific key combinations for input actions. | Purpose: Allows players to use custom key shortcuts for better control.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 31f0d519865de0062ac54d722798831473bcc170 to 36ceb6399c8f5bff235c3ccad3777870bdaec352 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 22:57:23 to 01/22/2026 22:59:18 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 31f0d519865de0062ac54d722798831473bcc170 to 36ceb6399c8f5bff235c3ccad3777870bdaec352 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 22:57:23 to 01/22/2026 22:59:18 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 3e7e1887a - 2026-01-22 16:57:44 -0600 - 01/22/2026 16:57:44
Added in Other:
- FFlagAppChatSuppressGroupOSAContextCard_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T22:55:37 | Mechanism: Suppresses certain context cards in group chats within the app. | Purpose: Reduces distractions in group chats, allowing for smoother communication among players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from afdd5cfcbc87c4e2288ea3e7fa7f2c76944704d1 to 31f0d519865de0062ac54d722798831473bcc170 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 22:52:08 to 01/22/2026 22:57:23 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from afdd5cfcbc87c4e2288ea3e7fa7f2c76944704d1 to 31f0d519865de0062ac54d722798831473bcc170 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 22:52:08 to 01/22/2026 22:57:23 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## b1e57be72 - 2026-01-22 16:53:14 -0600 - 01/22/2026 16:53:14
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from e65b73bb9e2ac70d687c656e5c3fb04010b64da5 to afdd5cfcbc87c4e2288ea3e7fa7f2c76944704d1 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 22:42:15 to 01/22/2026 22:52:08 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FFlagDeprecatePrecomputeDeformedVertices changed from False to True | Mechanism: Removes the use of precomputed vertex data for deformed models. | Purpose: Simplifies model processing, potentially improving performance in games.
- FStringFlagRepoGitHashFastString changed from e65b73bb9e2ac70d687c656e5c3fb04010b64da5 to afdd5cfcbc87c4e2288ea3e7fa7f2c76944704d1 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 22:42:15 to 01/22/2026 22:52:08 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagDeprecatePrecomputeDeformedVertices_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T21:47:17) | Mechanism: Phases out a method for calculating vertex deformations in models. | Purpose: Streamlines model rendering for better performance in games.

## 308636261 - 2026-01-22 16:44:20 -0600 - 01/22/2026 16:44:20
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 84e75b86880899108b7bcaedbdca9a5a9868e57c to e65b73bb9e2ac70d687c656e5c3fb04010b64da5 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 22:22:51 to 01/22/2026 22:42:15 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 84e75b86880899108b7bcaedbdca9a5a9868e57c to e65b73bb9e2ac70d687c656e5c3fb04010b64da5 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 22:22:51 to 01/22/2026 22:42:15 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## bed924ae5 - 2026-01-22 16:24:17 -0600 - 01/22/2026 16:24:17
Added in Other:
- FFlagAppChatGroupOsaAnalytics3_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T22:21:53 | Mechanism: Enhances analytics tracking for group chat features. | Purpose: Provides better insights into group chat usage, improving future updates and features.
Added in Camera/UI:
- FFlagLoadStoredInputAudioDeviceEarlier_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T22:21:20 | Mechanism: Loads the player's audio device settings sooner during startup. | Purpose: Ensures audio settings are ready faster, enhancing the audio experience for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 0cb7c870737f3cb05b9d14227933e85c066157e9 to 84e75b86880899108b7bcaedbdca9a5a9868e57c | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 22:16:55 to 01/22/2026 22:22:51 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 0cb7c870737f3cb05b9d14227933e85c066157e9 to 84e75b86880899108b7bcaedbdca9a5a9868e57c | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 22:16:55 to 01/22/2026 22:22:51 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 64041341b - 2026-01-22 16:17:23 -0600 - 01/22/2026 16:17:23
Added in Other:
- DFIntDataStoreUseStartupThrottlerSeconds = 30 | Mechanism: Sets a specific time limit for how long to throttle data store requests during startup. | Purpose: Allows developers to control the balance between speed and reliability when loading game data.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from bca36a34cfa6ebfa0ed2f338c8f5deddab38b765 to 0cb7c870737f3cb05b9d14227933e85c066157e9 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 22:14:01 to 01/22/2026 22:16:55 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from bca36a34cfa6ebfa0ed2f338c8f5deddab38b765 to 0cb7c870737f3cb05b9d14227933e85c066157e9 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 22:14:01 to 01/22/2026 22:16:55 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- DFIntDataStoreUseStartupThrottlerSeconds_Staged removed (was 30;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;false;1671199340;2026-01-22T21:14:20) | Mechanism: Limits the speed at which data is loaded at startup. | Purpose: Enhances game stability by preventing overload during startup.

## bb8ff6153 - 2026-01-22 16:15:06 -0600 - 01/22/2026 16:15:05
Added in Other:
- FFlagAppChatGroupOsaNavigateBeforeRecordDecline_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T22:12:10 | Mechanism: Modifies navigation flow in the chat app before declining a recording. | Purpose: Streamlines user experience when managing chat recordings.
- FFlagEventIngestTreatAcceptedAsSuccess_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T22:12:55 | Mechanism: Changes how event responses are processed to recognize accepted events as successful. | Purpose: Enhances event handling, making it clearer when actions are completed successfully.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 7639acc17c0b20bc5a39186cc300c8c09783e3f6 to bca36a34cfa6ebfa0ed2f338c8f5deddab38b765 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 22:11:30 to 01/22/2026 22:14:01 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 7639acc17c0b20bc5a39186cc300c8c09783e3f6 to bca36a34cfa6ebfa0ed2f338c8f5deddab38b765 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 22:11:30 to 01/22/2026 22:14:01 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 3f15c6bf2 - 2026-01-22 16:12:48 -0600 - 01/22/2026 16:12:48
Added in Other:
- FFlagAppChatNavigateBackIfOSAUnacknowledged_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T22:09:42 | Mechanism: Allows users to navigate back in chat if the app's on-screen actions are not acknowledged. | Purpose: Improves user experience by letting players easily return to previous chat messages.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from be2fc4eb15d8b6ab7acc4e20cdd09d3b557d5e9a to 7639acc17c0b20bc5a39186cc300c8c09783e3f6 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 22:09:05 to 01/22/2026 22:11:30 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from be2fc4eb15d8b6ab7acc4e20cdd09d3b557d5e9a to 7639acc17c0b20bc5a39186cc300c8c09783e3f6 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 22:09:05 to 01/22/2026 22:11:30 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## c5d226396 - 2026-01-22 16:10:32 -0600 - 01/22/2026 16:10:32
Added in Other:
- FFlagAppChatEnableGroupOSA3_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T22:08:16 | Mechanism: Activates a new chat system for group interactions. | Purpose: Enhances communication among group members, making it easier to collaborate in games.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 193f9660be6f857b1a9f1e1ef78aa746f73f0d67 to be2fc4eb15d8b6ab7acc4e20cdd09d3b557d5e9a | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 22:05:19 to 01/22/2026 22:09:05 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 193f9660be6f857b1a9f1e1ef78aa746f73f0d67 to be2fc4eb15d8b6ab7acc4e20cdd09d3b557d5e9a | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 22:05:19 to 01/22/2026 22:09:05 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 7cc0b53d3 - 2026-01-22 16:08:15 -0600 - 01/22/2026 16:08:15
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from b50c24c01cb536ff0488c55a85c727e64a8f5673 to 193f9660be6f857b1a9f1e1ef78aa746f73f0d67 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 22:02:00 to 01/22/2026 22:05:19 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from b50c24c01cb536ff0488c55a85c727e64a8f5673 to 193f9660be6f857b1a9f1e1ef78aa746f73f0d67 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 22:02:00 to 01/22/2026 22:05:19 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 7405358f4 - 2026-01-22 16:03:46 -0600 - 01/22/2026 16:03:46
Added in Other:
- DFIntReverbEnclosedKneeHundreths = 55 | Mechanism: Adjusts audio reverb settings for enclosed spaces. | Purpose: Enhances sound quality in enclosed areas, making audio more immersive.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from d733edbe19b74ff0430cb6f6d1b62ecbfdd8e920 to b50c24c01cb536ff0488c55a85c727e64a8f5673 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 21:57:12 to 01/22/2026 22:02:00 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from d733edbe19b74ff0430cb6f6d1b62ecbfdd8e920 to b50c24c01cb536ff0488c55a85c727e64a8f5673 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 21:57:12 to 01/22/2026 22:02:00 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- DFIntReverbEnclosedKneeHundreths_Staged removed (was 55;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;false;2039696775;2026-01-22T20:59:22) | Mechanism: Adjusts audio reverb settings based on enclosed space parameters. | Purpose: Enhances the audio experience in enclosed game environments.

## 3aa24ce8c - 2026-01-22 15:59:18 -0600 - 01/22/2026 15:59:18
Added in Other:
- DFIntRbxTelemetryBaseMultiplier_IXP = 1;Engine.Telemetry;engine_telemetry_retry_logic;830981440;flagbank | Mechanism: Adjusts the base multiplier for telemetry data collection. | Purpose: Improves data accuracy for better game performance insights.
- DFIntRbxTelemetryBaseRetryRandomOffsetRangeMs_IXP = 1;Engine.Telemetry;engine_telemetry_retry_logic;830981440;flagbank | Mechanism: Adjusts the retry timing for telemetry data collection. | Purpose: Improves data accuracy and reliability for game analytics.
- DFIntRbxTelemetryBaseRetryTimeMs_IXP = 1;Engine.Telemetry;engine_telemetry_retry_logic;830981440;flagbank | Mechanism: Sets a retry time for telemetry data collection. | Purpose: Improves the reliability of data tracking for better game performance insights.
- DFIntRbxTelemetryMaxBackoffTimeMs_IXP = 1;Engine.Telemetry;engine_telemetry_retry_logic;830981440;flagbank | Mechanism: Sets a maximum wait time for telemetry data to be sent if there are issues. | Purpose: Ensures smoother data reporting, which helps improve game performance for players.
- DFIntRbxTelemetryMaxConcurrentRetriedRequests_IXP = 1;Engine.Telemetry;engine_telemetry_retry_logic;830981440;flagbank | Mechanism: Sets a limit on the number of concurrent retried telemetry requests. | Purpose: Optimizes data collection processes, leading to improved game performance and stability.
- DFIntRbxTelemetryMaxElapsedTimeMs_IXP = 1;Engine.Telemetry;engine_telemetry_retry_logic;830981440;flagbank | Mechanism: Sets a maximum time limit for tracking game performance data. | Purpose: Helps developers monitor game performance more effectively.
- DFIntRbxTelemetryMaxRetryAttempts_IXP = 1;Engine.Telemetry;engine_telemetry_retry_logic;830981440;flagbank | Mechanism: Sets a limit on the number of retry attempts for telemetry data transmission. | Purpose: Ensures more reliable data collection without overwhelming the system.
- FFlagRbxTelemetryEnableHttpRetries3_IXP = 1;Engine.Telemetry;engine_telemetry_retry_logic;830981440;flagbank | Mechanism: Allows the system to retry HTTP requests up to three times if they fail. | Purpose: Enhances reliability of data transmission, reducing errors for players.
- FFlagTelemetryRetryOnConnectFail_IXP = 1;Engine.Telemetry;engine_telemetry_retry_logic;830981440;flagbank | Mechanism: Retries telemetry data transmission if the initial connection fails. | Purpose: Ensures more reliable data collection for better game performance insights.
- FFlagTelemetryRetryOnDnsResolve_IXP = 1;Engine.Telemetry;engine_telemetry_retry_logic;830981440;flagbank | Mechanism: Retries DNS resolution for telemetry data if it fails initially. | Purpose: Ensures more reliable tracking of player activity and system performance.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 185ab7a5ec03480617ee4c3df6dcacab53fd70c2 to d733edbe19b74ff0430cb6f6d1b62ecbfdd8e920 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 21:54:44 to 01/22/2026 21:57:12 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 185ab7a5ec03480617ee4c3df6dcacab53fd70c2 to d733edbe19b74ff0430cb6f6d1b62ecbfdd8e920 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 21:54:44 to 01/22/2026 21:57:12 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## d48e23550 - 2026-01-22 15:57:03 -0600 - 01/22/2026 15:57:03
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from c8bb5bfaac62e4893ea681d33117b4e2a5f426ea to 185ab7a5ec03480617ee4c3df6dcacab53fd70c2 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 21:51:28 to 01/22/2026 21:54:44 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from c8bb5bfaac62e4893ea681d33117b4e2a5f426ea to 185ab7a5ec03480617ee4c3df6dcacab53fd70c2 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 21:51:28 to 01/22/2026 21:54:44 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## df616c407 - 2026-01-22 15:52:25 -0600 - 01/22/2026 15:52:25
Added in Other:
- FFlagWrapDeformerContextOutputFileMeshData7 = True | Mechanism: Modifies how mesh data is processed and outputted in the game engine. | Purpose: Enhances the visual quality of 3D models, leading to a more immersive gaming experience.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 68317a4843f4d59ec7e85cbd8447ce2b9cd66dd9 to c8bb5bfaac62e4893ea681d33117b4e2a5f426ea | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 21:47:57 to 01/22/2026 21:51:28 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 68317a4843f4d59ec7e85cbd8447ce2b9cd66dd9 to c8bb5bfaac62e4893ea681d33117b4e2a5f426ea | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 21:47:57 to 01/22/2026 21:51:28 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagWrapDeformerContextOutputFileMeshData7_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T20:46:09) | Mechanism: Improves the way mesh data is processed and handled in the game engine. | Purpose: Enhances the performance and quality of 3D models in games.

## 006719848 - 2026-01-22 15:50:10 -0600 - 01/22/2026 15:50:10
Added in Other:
- FFlagDeprecatePrecomputeDeformedVertices_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T21:47:17 | Mechanism: Phases out a method for calculating vertex deformations in models. | Purpose: Streamlines model rendering for better performance in games.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 62925d8c45030d5f572c94103bc8c6a938f6da5e to 68317a4843f4d59ec7e85cbd8447ce2b9cd66dd9 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 21:46:45 to 01/22/2026 21:47:57 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 62925d8c45030d5f572c94103bc8c6a938f6da5e to 68317a4843f4d59ec7e85cbd8447ce2b9cd66dd9 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 21:46:45 to 01/22/2026 21:47:57 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 211aa2545 - 2026-01-22 15:47:55 -0600 - 01/22/2026 15:47:55
Added in Other:
- FFlagMoveDeviceInfoLater = True | Mechanism: Delays the loading of device information until after the game starts. | Purpose: Improves game loading speed for players, making it feel faster.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 46676076bb39a399a6bae89fd2b83520be3055ce to 62925d8c45030d5f572c94103bc8c6a938f6da5e | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 21:38:05 to 01/22/2026 21:46:45 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 46676076bb39a399a6bae89fd2b83520be3055ce to 62925d8c45030d5f572c94103bc8c6a938f6da5e | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 21:38:05 to 01/22/2026 21:46:45 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagExperiencesOnProfile_v2_Staged removed (was true;SteadyState;10;30;Revert;true;1289119975;2026-01-22T21:10:42) | Mechanism: Enables a new layout for displaying experiences on user profiles. | Purpose: Makes it easier for players to find and showcase their favorite games.
- FFlagExperiencesOnProfileIxpEnabled_Staged removed (was true;SteadyState;10;30;Revert;true;1289119975;2026-01-22T21:10:42) | Mechanism: Displays user experiences directly on their profile page. | Purpose: Makes it easier for players to find and access games created by their friends.
- FFlagMoveDeviceInfoLater_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T20:40:27) | Mechanism: Delays the loading of device information until it's needed. | Purpose: Optimizes performance by reducing initial load times, leading to a smoother gameplay experience.
- FStringExperiencesOnProfileIxpLayer_Staged removed (was Social.Profile;SteadyState;10;30;Revert;true;1289119975;2026-01-22T21:10:42) | Mechanism: Changes how experiences are displayed on player profiles. | Purpose: Enhances visibility of player experiences, making it easier for others to discover games.

## 054b51aec - 2026-01-22 15:39:06 -0600 - 01/22/2026 15:39:05
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 074af2792b7eb7779f7393c87b9facaf3bea5f46 to 46676076bb39a399a6bae89fd2b83520be3055ce | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 21:32:06 to 01/22/2026 21:38:05 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 074af2792b7eb7779f7393c87b9facaf3bea5f46 to 46676076bb39a399a6bae89fd2b83520be3055ce | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 21:32:06 to 01/22/2026 21:38:05 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 2cc46e01d - 2026-01-22 15:34:39 -0600 - 01/22/2026 15:34:39
Added in Other:
- DFFlagVideoCaptureDropNegativePts = True | Mechanism: Adjusts video capture settings to ignore negative timestamps. | Purpose: Improves video recording quality by ensuring only valid frames are captured.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 7bddf89c51235fd1681bffcbbabc55eacd07fa93 to 074af2792b7eb7779f7393c87b9facaf3bea5f46 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 21:26:44 to 01/22/2026 21:32:06 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 7bddf89c51235fd1681bffcbbabc55eacd07fa93 to 074af2792b7eb7779f7393c87b9facaf3bea5f46 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 21:26:44 to 01/22/2026 21:32:06 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- DFFlagVideoCaptureDropNegativePts_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T20:26:33) | Mechanism: Removes negative timestamps from video capture data. | Purpose: Improves video playback quality by ensuring accurate timing.

## 87d84a292 - 2026-01-22 15:27:53 -0600 - 01/22/2026 15:27:53
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from d8c281c54e0f85de6555e6de785973c0c0e2f932 to 7bddf89c51235fd1681bffcbbabc55eacd07fa93 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 21:21:48 to 01/22/2026 21:26:44 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from d8c281c54e0f85de6555e6de785973c0c0e2f932 to 7bddf89c51235fd1681bffcbbabc55eacd07fa93 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 21:21:48 to 01/22/2026 21:26:44 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 0af66678c - 2026-01-22 15:23:25 -0600 - 01/22/2026 15:23:25
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 63b3a3c12c9de0fa36c78977fc9e7254eb068c60 to d8c281c54e0f85de6555e6de785973c0c0e2f932 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 21:16:29 to 01/22/2026 21:21:48 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 63b3a3c12c9de0fa36c78977fc9e7254eb068c60 to d8c281c54e0f85de6555e6de785973c0c0e2f932 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 21:16:29 to 01/22/2026 21:21:48 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 5da8ea500 - 2026-01-22 15:18:49 -0600 - 01/22/2026 15:18:48
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 8dc2dca152f24850a7dd32363229f2d38c20a9c8 to 63b3a3c12c9de0fa36c78977fc9e7254eb068c60 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 21:15:23 to 01/22/2026 21:16:29 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 8dc2dca152f24850a7dd32363229f2d38c20a9c8 to 63b3a3c12c9de0fa36c78977fc9e7254eb068c60 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 21:15:23 to 01/22/2026 21:16:29 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## d30357f33 - 2026-01-22 15:16:34 -0600 - 01/22/2026 15:16:34
Added in Other:
- DFIntDataStoreUseStartupThrottlerSeconds_Staged = 30;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;false;1671199340;2026-01-22T21:14:20 | Mechanism: Limits the speed at which data is loaded at startup. | Purpose: Enhances game stability by preventing overload during startup.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 44da1b360cfade18c1f673be7bc96154867698ae to 8dc2dca152f24850a7dd32363229f2d38c20a9c8 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 21:12:11 to 01/22/2026 21:15:23 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 44da1b360cfade18c1f673be7bc96154867698ae to 8dc2dca152f24850a7dd32363229f2d38c20a9c8 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 21:12:11 to 01/22/2026 21:15:23 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## fc2059636 - 2026-01-22 15:14:19 -0600 - 01/22/2026 15:14:19
Added in Other:
- FFlagExperiencesOnProfile_v2_IXP = 1;Social.Profile;Social.Profile.ExperiencesOnProfile_v2;1289119975;dev_controlled | Mechanism: Updates the way experiences are displayed on user profiles. | Purpose: Provides a more modern and user-friendly interface for viewing experiences.
- FFlagExperiencesOnProfile_v2_Staged = true;SteadyState;10;30;Revert;true;1289119975;2026-01-22T21:10:42 | Mechanism: Enables a new layout for displaying experiences on user profiles. | Purpose: Makes it easier for players to find and showcase their favorite games.
- FFlagExperiencesOnProfileIxpEnabled_IXP = 1;Social.Profile;Social.Profile.ExperiencesOnProfile_v2;1289119975;dev_controlled | Mechanism: Enables displaying user experiences directly on profiles. | Purpose: Allows players to easily find and access games created by users on their profiles.
- FFlagExperiencesOnProfileIxpEnabled_Staged = true;SteadyState;10;30;Revert;true;1289119975;2026-01-22T21:10:42 | Mechanism: Displays user experiences directly on their profile page. | Purpose: Makes it easier for players to find and access games created by their friends.
- FStringExperiencesOnProfileIxpLayer_IXP = 1;Social.Profile;Social.Profile.ExperiencesOnProfile_v2;1289119975;dev_controlled | Mechanism: Enables a new layer for displaying user experiences on profiles. | Purpose: Improves how players see and access experiences on their profiles.
- FStringExperiencesOnProfileIxpLayer_Staged = Social.Profile;SteadyState;10;30;Revert;true;1289119975;2026-01-22T21:10:42 | Mechanism: Changes how experiences are displayed on player profiles. | Purpose: Enhances visibility of player experiences, making it easier for others to discover games.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from acff38f3fd3d1c3f8c0a3923455b68db47ffa1b1 to 44da1b360cfade18c1f673be7bc96154867698ae | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 21:08:42 to 01/22/2026 21:12:11 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from acff38f3fd3d1c3f8c0a3923455b68db47ffa1b1 to 44da1b360cfade18c1f673be7bc96154867698ae | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 21:08:42 to 01/22/2026 21:12:11 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## c64cc384f - 2026-01-22 15:09:51 -0600 - 01/22/2026 15:09:51
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 6d7f4f1ea378f6e69f7888f316b490ed511924ed to acff38f3fd3d1c3f8c0a3923455b68db47ffa1b1 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 21:00:25 to 01/22/2026 21:08:42 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 6d7f4f1ea378f6e69f7888f316b490ed511924ed to acff38f3fd3d1c3f8c0a3923455b68db47ffa1b1 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 21:00:25 to 01/22/2026 21:08:42 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 693849ac6 - 2026-01-22 15:03:15 -0600 - 01/22/2026 15:03:15
Added in Other:
- DFIntReverbEnclosedKneeHundreths_Staged = 55;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;false;2039696775;2026-01-22T20:59:22 | Mechanism: Adjusts audio reverb settings based on enclosed space parameters. | Purpose: Enhances the audio experience in enclosed game environments.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 43ff7cd862f381b1467a638cb16176cfa3519a27 to 6d7f4f1ea378f6e69f7888f316b490ed511924ed | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 20:57:27 to 01/22/2026 21:00:25 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 43ff7cd862f381b1467a638cb16176cfa3519a27 to 6d7f4f1ea378f6e69f7888f316b490ed511924ed | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 20:57:27 to 01/22/2026 21:00:25 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 34bfd01df - 2026-01-22 14:58:49 -0600 - 01/22/2026 14:58:49
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from e4530211982b0b1d4d70d94851b855e54e987a53 to 43ff7cd862f381b1467a638cb16176cfa3519a27 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 20:51:21 to 01/22/2026 20:57:27 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from e4530211982b0b1d4d70d94851b855e54e987a53 to 43ff7cd862f381b1467a638cb16176cfa3519a27 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 20:51:21 to 01/22/2026 20:57:27 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 7da210022 - 2026-01-22 14:52:09 -0600 - 01/22/2026 14:52:08
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 11999bafb3d8f92600f3d5203bb8839e63e5a9e9 to e4530211982b0b1d4d70d94851b855e54e987a53 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 20:46:47 to 01/22/2026 20:51:21 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 11999bafb3d8f92600f3d5203bb8839e63e5a9e9 to e4530211982b0b1d4d70d94851b855e54e987a53 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 20:46:47 to 01/22/2026 20:51:21 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 9cb147852 - 2026-01-22 14:47:43 -0600 - 01/22/2026 14:47:43
Added in Other:
- FFlagWrapDeformerContextOutputFileMeshData7_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T20:46:09 | Mechanism: Improves the way mesh data is processed and handled in the game engine. | Purpose: Enhances the performance and quality of 3D models in games.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 2e016b7abe5b88952c9f94dad223a91e0075b7a7 to 11999bafb3d8f92600f3d5203bb8839e63e5a9e9 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 20:41:59 to 01/22/2026 20:46:47 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 2e016b7abe5b88952c9f94dad223a91e0075b7a7 to 11999bafb3d8f92600f3d5203bb8839e63e5a9e9 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 20:41:59 to 01/22/2026 20:46:47 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## fa891fa6b - 2026-01-22 14:43:16 -0600 - 01/22/2026 14:43:16
Added in Other:
- FFlagLuauCodegenVectorCreateXy = True | Mechanism: Enhances the code generation for creating 2D vectors in Luau. | Purpose: Makes it easier for developers to work with 2D graphics in their games.
- FFlagMoveDeviceInfoLater_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T20:40:27 | Mechanism: Delays the loading of device information until it's needed. | Purpose: Optimizes performance by reducing initial load times, leading to a smoother gameplay experience.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 991f1c7629493c09bc085af6f594457910805f30 to 2e016b7abe5b88952c9f94dad223a91e0075b7a7 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 20:36:27 to 01/22/2026 20:41:59 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 991f1c7629493c09bc085af6f594457910805f30 to 2e016b7abe5b88952c9f94dad223a91e0075b7a7 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 20:36:27 to 01/22/2026 20:41:59 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagLuauCodegenVectorCreateXy_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T19:39:42) | Mechanism: Introduces a new way to create 2D vectors in Luau code. | Purpose: Simplifies coding for developers by making it easier to work with 2D vector coordinates.

## c3040de6c - 2026-01-22 14:38:52 -0600 - 01/22/2026 14:38:51
Added in Other:
- DFFlagRCCSetLimitsParseNumbers = True | Mechanism: Allows the system to interpret and set numerical limits in a more flexible way. | Purpose: Enhances user experience by making it easier to manage and set numerical values in games.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 5dc4025ba3520ce41c5fa54b72575dacff2f2c83 to 991f1c7629493c09bc085af6f594457910805f30 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 20:31:14 to 01/22/2026 20:36:27 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 5dc4025ba3520ce41c5fa54b72575dacff2f2c83 to 991f1c7629493c09bc085af6f594457910805f30 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 20:31:14 to 01/22/2026 20:36:27 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- DFFlagRCCSetLimitsParseNumbers_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T19:34:19) | Mechanism: Adjusts how numerical limits are parsed in the game settings. | Purpose: Allows for more accurate game settings and configurations for players.

## 9dd3b7b31 - 2026-01-22 14:32:11 -0600 - 01/22/2026 14:32:10
Added in Body:
- FFlagCharacterBreakJointsOnDeath = True | Mechanism: Causes character joints to break when a player’s character dies. | Purpose: Adds a more realistic and immersive effect to character death animations.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 6e62e26231db9115e8f09f0d33bd922b98721d1d to 5dc4025ba3520ce41c5fa54b72575dacff2f2c83 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 20:27:54 to 01/22/2026 20:31:14 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 6e62e26231db9115e8f09f0d33bd922b98721d1d to 5dc4025ba3520ce41c5fa54b72575dacff2f2c83 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 20:27:54 to 01/22/2026 20:31:14 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Body:
- FFlagCharacterBreakJointsOnDeath_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T19:26:23) | Mechanism: Changes how character joints behave when a character dies. | Purpose: Adds a more realistic effect to character deaths, enhancing visual feedback.

## c664d298b - 2026-01-22 14:29:54 -0600 - 01/22/2026 14:29:53
Added in Other:
- DFFlagVideoCaptureDropNegativePts_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T20:26:33 | Mechanism: Removes negative timestamps from video capture data. | Purpose: Improves video playback quality by ensuring accurate timing.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from b241cf8c74a686af41a5493e783727cd4c55216e to 6e62e26231db9115e8f09f0d33bd922b98721d1d | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 20:26:34 to 01/22/2026 20:27:54 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from b241cf8c74a686af41a5493e783727cd4c55216e to 6e62e26231db9115e8f09f0d33bd922b98721d1d | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 20:26:34 to 01/22/2026 20:27:54 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## fc855c94a - 2026-01-22 14:27:28 -0600 - 01/22/2026 14:27:28
Changed in Other:
- DFFlagProductInfoBatchingResponseValidationAnalyticsEnabled2 changed from True to False | Mechanism: Validates and batches product information responses for analytics. | Purpose: Improves the accuracy of product data tracking for better user experience.
- DFStringFlagRepoGitHashDynamicString changed from 9967bb8b84efe26efbdf9f9db84206877a298b33 to b241cf8c74a686af41a5493e783727cd4c55216e | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 20:21:27 to 01/22/2026 20:26:34 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 9967bb8b84efe26efbdf9f9db84206877a298b33 to b241cf8c74a686af41a5493e783727cd4c55216e | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 20:21:27 to 01/22/2026 20:26:34 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- DFFlagProductInfoBatchingResponseValidationAnalyticsEnabled2_Staged removed (was false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T19:24:28) | Mechanism: Enhances the validation process for product info responses in batches. | Purpose: Ensures players receive accurate product information quickly, improving shopping experience.

## 8541e57d6 - 2026-01-22 14:23:03 -0600 - 01/22/2026 14:23:03
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 89cdaf6221118992b47886c7625f2964ceda9b75 to 9967bb8b84efe26efbdf9f9db84206877a298b33 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 20:16:37 to 01/22/2026 20:21:27 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 89cdaf6221118992b47886c7625f2964ceda9b75 to 9967bb8b84efe26efbdf9f9db84206877a298b33 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 20:16:37 to 01/22/2026 20:21:27 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## df10acfda - 2026-01-22 14:18:39 -0600 - 01/22/2026 14:18:39
Added in Physics:
- DFFlagAuroraAutoPredictHumanoidsAndModels3 = True | Mechanism: Enhances prediction algorithms for humanoids and models in the Aurora system. | Purpose: Improves the accuracy of character and model movements, making gameplay smoother.
- DFFlagForceValidHttpRequestPriority = True | Mechanism: Ensures that HTTP requests are prioritized based on their validity. | Purpose: Improves the reliability of network requests, leading to a smoother gameplay experience.
Added in Other:
- DFFlagStreamingHandleInvalidValues = True | Mechanism: Implements checks to manage unexpected or invalid data during streaming. | Purpose: Enhances game stability and reduces errors for players during gameplay.
Added in Body:
- FFlagLcFmdIgnoreEditableBodyPart = True | Mechanism: Ignores certain editable body parts in the character model. | Purpose: Streamlines character customization and reduces potential issues.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from d5728e985bc27421ed4dd3f3c14e874df51a358a to 89cdaf6221118992b47886c7625f2964ceda9b75 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 20:15:37 to 01/22/2026 20:16:37 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from d5728e985bc27421ed4dd3f3c14e874df51a358a to 89cdaf6221118992b47886c7625f2964ceda9b75 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 20:15:37 to 01/22/2026 20:16:37 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Physics:
- DFFlagAuroraAutoPredictHumanoidsAndModels3_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T19:12:29) | Mechanism: Enhances the prediction algorithms for humanoid and model interactions in the game engine. | Purpose: Improves gameplay by making character movements and interactions smoother and more realistic.
- DFFlagForceValidHttpRequestPriority_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T19:13:59) | Mechanism: Prioritizes valid HTTP requests for processing. | Purpose: Enhances the speed and efficiency of online interactions in games.
Removed in Other:
- DFFlagStreamingHandleInvalidValues_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T19:12:27) | Mechanism: Handles invalid data values during streaming more effectively. | Purpose: Reduces errors and improves the overall streaming experience for players.
Removed in Body:
- FFlagLcFmdIgnoreEditableBodyPart_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T19:12:37) | Mechanism: Modifies how editable body parts are treated in the game engine. | Purpose: Allows for better customization options without affecting gameplay mechanics.

## 1ac7cc5c7 - 2026-01-22 14:16:25 -0600 - 01/22/2026 14:16:25
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 51ae763e57cf0be2d7cb498005dc4efabe8f5d66 to d5728e985bc27421ed4dd3f3c14e874df51a358a | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 20:13:02 to 01/22/2026 20:15:37 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 51ae763e57cf0be2d7cb498005dc4efabe8f5d66 to d5728e985bc27421ed4dd3f3c14e874df51a358a | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 20:13:02 to 01/22/2026 20:15:37 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 9b0810e4e - 2026-01-22 14:14:11 -0600 - 01/22/2026 14:14:10
Added in Other:
- FFlagLsbOptimization2 = True | Mechanism: Improves the efficiency of data processing in the game engine. | Purpose: Reduces lag and improves game performance for smoother gameplay.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from e14e838cd915190f5a04e3d8146b9319cd353639 to 51ae763e57cf0be2d7cb498005dc4efabe8f5d66 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 20:06:19 to 01/22/2026 20:13:02 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from e14e838cd915190f5a04e3d8146b9319cd353639 to 51ae763e57cf0be2d7cb498005dc4efabe8f5d66 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 20:06:19 to 01/22/2026 20:13:02 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagLsbOptimization2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T19:10:03) | Mechanism: Implements optimizations for loading and processing game assets. | Purpose: Improves game performance and reduces loading times for players.

## c5bd6d3ab - 2026-01-22 14:07:32 -0600 - 01/22/2026 14:07:31
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 12a3c4756482904fd223935d892c81450e7c7e16 to e14e838cd915190f5a04e3d8146b9319cd353639 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 20:01:55 to 01/22/2026 20:06:19 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 12a3c4756482904fd223935d892c81450e7c7e16 to e14e838cd915190f5a04e3d8146b9319cd353639 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 20:01:55 to 01/22/2026 20:06:19 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 24781bcf9 - 2026-01-22 14:03:06 -0600 - 01/22/2026 14:03:05
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from c93687a9e8639b575a4b0d81c398dc732136b7e7 to 12a3c4756482904fd223935d892c81450e7c7e16 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 19:56:48 to 01/22/2026 20:01:55 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from c93687a9e8639b575a4b0d81c398dc732136b7e7 to 12a3c4756482904fd223935d892c81450e7c7e16 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 19:56:48 to 01/22/2026 20:01:55 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## cb216ed76 - 2026-01-22 13:58:34 -0600 - 01/22/2026 13:58:34
Changed in Physics:
- DFIntSimAnimationConstraintResponsiveness changed from 100 to 50 | Mechanism: Adjusts the responsiveness of animation constraints in the simulation. | Purpose: Improves the fluidity and responsiveness of character animations in games.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 58e3a588a7635607fbb624d9412b91dddc4aea31 to c93687a9e8639b575a4b0d81c398dc732136b7e7 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 19:51:47 to 01/22/2026 19:56:48 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 58e3a588a7635607fbb624d9412b91dddc4aea31 to c93687a9e8639b575a4b0d81c398dc732136b7e7 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 19:51:47 to 01/22/2026 19:56:48 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Physics:
- DFIntSimAnimationConstraintResponsiveness_Staged removed (was 50;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T18:55:06) | Mechanism: Adjusts the responsiveness of animation constraints in simulations. | Purpose: Enhances the fluidity and responsiveness of character animations during gameplay.

## c13e11242 - 2026-01-22 13:54:06 -0600 - 01/22/2026 13:54:06
Added in Camera/UI:
- FFlagLuaStartPageBuilderIcons2 = True | Mechanism: Updates the icons on the Lua start page for better visibility. | Purpose: Makes it easier for developers to find and use tools when creating games.
Added in Other:
- FFlagLuaStartPageFoundationPill = True | Mechanism: Implements a new foundational structure for the Lua start page. | Purpose: Improves the user experience for developers using Lua by making navigation simpler.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 34ef5e167b0e98e91116876a4970ac1a685a616b to 58e3a588a7635607fbb624d9412b91dddc4aea31 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 19:47:28 to 01/22/2026 19:51:47 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 34ef5e167b0e98e91116876a4970ac1a685a616b to 58e3a588a7635607fbb624d9412b91dddc4aea31 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 19:47:28 to 01/22/2026 19:51:47 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Camera/UI:
- FFlagLuaStartPageBuilderIcons2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T18:46:10) | Mechanism: Enables new icons for the page builder in Lua scripts. | Purpose: Improves the visual experience for developers using the page builder.
Removed in Other:
- FFlagLuaStartPageFoundationPill_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T18:47:43) | Mechanism: Updates the starting page for Lua scripting with a new design. | Purpose: Provides a better user experience for developers learning to script in Roblox.

## 033b0a1df - 2026-01-22 13:49:38 -0600 - 01/22/2026 13:49:38
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from d54ce67bd19d7fdab7db21fc9896fa1278519610 to 34ef5e167b0e98e91116876a4970ac1a685a616b | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 19:41:35 to 01/22/2026 19:47:28 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from d54ce67bd19d7fdab7db21fc9896fa1278519610 to 34ef5e167b0e98e91116876a4970ac1a685a616b | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 19:41:35 to 01/22/2026 19:47:28 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## dffefd4da - 2026-01-22 13:42:59 -0600 - 01/22/2026 13:42:59
Added in Other:
- FFlagLuauCodegenVectorCreateXy_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T19:39:42 | Mechanism: Introduces a new way to create 2D vectors in Luau code. | Purpose: Simplifies coding for developers by making it easier to work with 2D vector coordinates.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from f43fc4f5a045eeafb53ec5c172fa3e7d0396f59d to d54ce67bd19d7fdab7db21fc9896fa1278519610 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 19:35:23 to 01/22/2026 19:41:35 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from f43fc4f5a045eeafb53ec5c172fa3e7d0396f59d to d54ce67bd19d7fdab7db21fc9896fa1278519610 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 19:35:23 to 01/22/2026 19:41:35 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 0e99f17aa - 2026-01-22 13:36:19 -0600 - 01/22/2026 13:36:19
Added in Other:
- DFFlagRCCSetLimitsParseNumbers_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T19:34:19 | Mechanism: Adjusts how numerical limits are parsed in the game settings. | Purpose: Allows for more accurate game settings and configurations for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from fce7bd3f076f87907c07b4ed0148ea0c737e127d to f43fc4f5a045eeafb53ec5c172fa3e7d0396f59d | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 19:32:58 to 01/22/2026 19:35:23 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from fce7bd3f076f87907c07b4ed0148ea0c737e127d to f43fc4f5a045eeafb53ec5c172fa3e7d0396f59d | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 19:32:58 to 01/22/2026 19:35:23 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 5c09bf1c1 - 2026-01-22 13:34:03 -0600 - 01/22/2026 13:34:03
Added in Other:
- FFlagRemoveBackendAdsDestructor = True | Mechanism: Removes a component that cleans up ad-related backend processes. | Purpose: Improves ad stability and performance for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from dfbe7114d66ce549094017411814dcfc6b4de10b to fce7bd3f076f87907c07b4ed0148ea0c737e127d | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 19:29:35 to 01/22/2026 19:32:58 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from dfbe7114d66ce549094017411814dcfc6b4de10b to fce7bd3f076f87907c07b4ed0148ea0c737e127d | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 19:29:35 to 01/22/2026 19:32:58 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagIASModifierKeys_Staged removed (was true;SteadyState;10;30;Revert;2026-01-22T18:56:51) | Mechanism: Enables specific key combinations for input actions. | Purpose: Allows players to use custom key shortcuts for better control.
- FFlagRemoveBackendAdsDestructor_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;338665152;2026-01-22T18:29:52) | Mechanism: Eliminates a component that was responsible for managing backend ads. | Purpose: Reduces clutter and potential issues related to ads, leading to a smoother gameplay experience.

## f39eaf6bc - 2026-01-22 13:31:46 -0600 - 01/22/2026 13:31:46
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 3a05759bcee95bb49f2cc73b433c63b58ab28259 to dfbe7114d66ce549094017411814dcfc6b4de10b | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 19:28:05 to 01/22/2026 19:29:35 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 3a05759bcee95bb49f2cc73b433c63b58ab28259 to dfbe7114d66ce549094017411814dcfc6b4de10b | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 19:28:05 to 01/22/2026 19:29:35 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 3de7b930f - 2026-01-22 13:29:30 -0600 - 01/22/2026 13:29:30
Added in Body:
- FFlagCharacterBreakJointsOnDeath_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T19:26:23 | Mechanism: Changes how character joints behave when a character dies. | Purpose: Adds a more realistic effect to character deaths, enhancing visual feedback.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from f84b0696bed9720ef06d73688fb457ccb254e4e3 to 3a05759bcee95bb49f2cc73b433c63b58ab28259 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 19:25:40 to 01/22/2026 19:28:05 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from f84b0696bed9720ef06d73688fb457ccb254e4e3 to 3a05759bcee95bb49f2cc73b433c63b58ab28259 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 19:25:40 to 01/22/2026 19:28:05 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 6c259dc0b - 2026-01-22 13:27:14 -0600 - 01/22/2026 13:27:14
Added in Other:
- DFFlagProductInfoBatchingResponseValidationAnalyticsEnabled2_Staged = false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T19:24:28 | Mechanism: Enhances the validation process for product info responses in batches. | Purpose: Ensures players receive accurate product information quickly, improving shopping experience.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from e08cc129252caf6b63219d7fdc5a240ec4aecb67 to f84b0696bed9720ef06d73688fb457ccb254e4e3 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 19:21:31 to 01/22/2026 19:25:40 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from e08cc129252caf6b63219d7fdc5a240ec4aecb67 to f84b0696bed9720ef06d73688fb457ccb254e4e3 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 19:21:31 to 01/22/2026 19:25:40 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## a840f84cc - 2026-01-22 13:22:47 -0600 - 01/22/2026 13:22:47
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from ed0f748a65be589a09ddb6994f9192cec05be66f to e08cc129252caf6b63219d7fdc5a240ec4aecb67 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 19:15:28 to 01/22/2026 19:21:31 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from ed0f748a65be589a09ddb6994f9192cec05be66f to e08cc129252caf6b63219d7fdc5a240ec4aecb67 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 19:15:28 to 01/22/2026 19:21:31 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 3bb7996bb - 2026-01-22 13:18:16 -0600 - 01/22/2026 13:18:16
Added in Input:
- FFlagTouchEventCodeRefactor = True | Mechanism: Reorganizes the code that handles touch events for better efficiency. | Purpose: Improves the responsiveness and reliability of touch controls in games.
Removed in Input:
- FFlagTouchEventCodeRefactor_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T18:10:44) | Mechanism: Improves the code handling touch events. | Purpose: Enhances responsiveness and accuracy of touch controls for players.

## f8cc9dee5 - 2026-01-22 13:16:01 -0600 - 01/22/2026 13:16:01
Added in Physics:
- DFFlagAuroraAutoPredictHumanoidsAndModels3_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T19:12:29 | Mechanism: Enhances the prediction algorithms for humanoid and model interactions in the game engine. | Purpose: Improves gameplay by making character movements and interactions smoother and more realistic.
- DFFlagForceValidHttpRequestPriority_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T19:13:59 | Mechanism: Prioritizes valid HTTP requests for processing. | Purpose: Enhances the speed and efficiency of online interactions in games.
Added in Body:
- FFlagLcFmdIgnoreEditableBodyPart_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T19:12:37 | Mechanism: Modifies how editable body parts are treated in the game engine. | Purpose: Allows for better customization options without affecting gameplay mechanics.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from de39125b0010725510ee9e7506b6296c4ccd39bc to ed0f748a65be589a09ddb6994f9192cec05be66f | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 19:13:32 to 01/22/2026 19:15:28 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from de39125b0010725510ee9e7506b6296c4ccd39bc to ed0f748a65be589a09ddb6994f9192cec05be66f | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 19:13:32 to 01/22/2026 19:15:28 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 7bb7f8065 - 2026-01-22 13:13:45 -0600 - 01/22/2026 13:13:45
Added in Other:
- DFFlagStreamingHandleInvalidValues_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T19:12:27 | Mechanism: Handles invalid data values during streaming more effectively. | Purpose: Reduces errors and improves the overall streaming experience for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 2bccf7c2565ba31914119c790243a972cb9983d7 to de39125b0010725510ee9e7506b6296c4ccd39bc | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 19:11:11 to 01/22/2026 19:13:32 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 2bccf7c2565ba31914119c790243a972cb9983d7 to de39125b0010725510ee9e7506b6296c4ccd39bc | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 19:11:11 to 01/22/2026 19:13:32 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Body:
- FFlagLcFmdIgnoreEditableBodyPart_Staged removed (was true;SteadyState;10;30;Revert;2026-01-22T18:39:58) | Mechanism: Modifies how editable body parts are treated in the game engine. | Purpose: Allows for better customization options without affecting gameplay mechanics.
Removed in Other:
- FFlagWrapDeformerContextOutputFileMeshData7_Staged removed (was true;SteadyState;10;30;Revert;2026-01-22T18:39:58) | Mechanism: Improves the way mesh data is processed and handled in the game engine. | Purpose: Enhances the performance and quality of 3D models in games.

## a0706cbb8 - 2026-01-22 13:11:30 -0600 - 01/22/2026 13:11:30
Added in Other:
- FFlagLsbOptimization2_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T19:10:03 | Mechanism: Implements optimizations for loading and processing game assets. | Purpose: Improves game performance and reduces loading times for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from d2ca150c011e15ede87c0f7714c249d30de57cc6 to 2bccf7c2565ba31914119c790243a972cb9983d7 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 19:07:07 to 01/22/2026 19:11:11 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from d2ca150c011e15ede87c0f7714c249d30de57cc6 to 2bccf7c2565ba31914119c790243a972cb9983d7 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 19:07:07 to 01/22/2026 19:11:11 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 4f4e9e73a - 2026-01-22 13:09:14 -0600 - 01/22/2026 13:09:13
Added in Other:
- FFlagStudioUpdateShutdownButton = True | Mechanism: Adds a button in the Studio to shut down updates. | Purpose: Allows developers to easily stop updates while working.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from b09fc09210354dc31e0b08c8c9cf495553110995 to d2ca150c011e15ede87c0f7714c249d30de57cc6 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 19:03:23 to 01/22/2026 19:07:07 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from b09fc09210354dc31e0b08c8c9cf495553110995 to d2ca150c011e15ede87c0f7714c249d30de57cc6 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 19:03:23 to 01/22/2026 19:07:07 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagStudioUpdateShutdownButton_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;73257166;2026-01-22T18:04:16) | Mechanism: Adds a button in Roblox Studio to easily shut down the application after updates. | Purpose: Makes it more convenient for developers to manage their workflow by quickly closing the Studio after updates.

## 1d1a3a79d - 2026-01-22 13:04:45 -0600 - 01/22/2026 13:04:45
Added in Graphics:
- FFlagRefactorTexturePackManagement2 = True | Mechanism: Improves how texture packs are organized and managed in the game. | Purpose: Enhances the overall performance and usability of texture packs for better visuals.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from f80c127e9e8214789ab8b3dce461139f9e0129bc to b09fc09210354dc31e0b08c8c9cf495553110995 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 19:01:49 to 01/22/2026 19:03:23 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from f80c127e9e8214789ab8b3dce461139f9e0129bc to b09fc09210354dc31e0b08c8c9cf495553110995 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 19:01:49 to 01/22/2026 19:03:23 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Graphics:
- FFlagRefactorTexturePackManagement2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T18:00:34) | Mechanism: Updates the system for managing texture packs in games. | Purpose: Makes it easier for developers to use and manage textures, improving game visuals.

## a954a9db8 - 2026-01-22 13:02:29 -0600 - 01/22/2026 13:02:29
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 14b4a59b07e6e5cf6abdb88e328ba6101866a238 to f80c127e9e8214789ab8b3dce461139f9e0129bc | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 18:58:15 to 01/22/2026 19:01:49 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 14b4a59b07e6e5cf6abdb88e328ba6101866a238 to f80c127e9e8214789ab8b3dce461139f9e0129bc | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 18:58:15 to 01/22/2026 19:01:49 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## f1d133f29 - 2026-01-22 13:00:13 -0600 - 01/22/2026 13:00:12
Added in Other:
- FFlagIASModifierKeys_Staged = true;SteadyState;10;30;Revert;2026-01-22T18:56:51 | Mechanism: Enables specific key combinations for input actions. | Purpose: Allows players to use custom key shortcuts for better control.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from f2e56573d288ea7969b9e9844cb9fb64e4c890c7 to 14b4a59b07e6e5cf6abdb88e328ba6101866a238 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 18:56:44 to 01/22/2026 18:58:15 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from f2e56573d288ea7969b9e9844cb9fb64e4c890c7 to 14b4a59b07e6e5cf6abdb88e328ba6101866a238 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 18:56:44 to 01/22/2026 18:58:15 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 7216d9b28 - 2026-01-22 12:57:54 -0600 - 01/22/2026 12:57:54
Added in Physics:
- DFIntSimAnimationConstraintResponsiveness_Staged = 50;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T18:55:06 | Mechanism: Adjusts the responsiveness of animation constraints in simulations. | Purpose: Enhances the fluidity and responsiveness of character animations during gameplay.
Added in Camera/UI:
- FIntStudioMenuOpenCooldownMillis = 200 | Mechanism: Sets a cooldown timer for opening the studio menu. | Purpose: Prevents spam clicking and enhances user experience in the studio.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 39e7cb3a77654caad8af0fc17bfe2316176ae0b9 to f2e56573d288ea7969b9e9844cb9fb64e4c890c7 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 18:49:13 to 01/22/2026 18:56:44 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 39e7cb3a77654caad8af0fc17bfe2316176ae0b9 to f2e56573d288ea7969b9e9844cb9fb64e4c890c7 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 18:49:13 to 01/22/2026 18:56:44 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Camera/UI:
- FIntStudioMenuOpenCooldownMillis_Staged removed (was 200;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T17:51:18) | Mechanism: Introduces a cooldown period for opening the studio menu. | Purpose: Prevents accidental menu openings, making it easier for developers to work.

## 59d220b76 - 2026-01-22 12:51:13 -0600 - 01/22/2026 12:51:13
Added in Other:
- FFlagLuaStartPageFoundationPill_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T18:47:43 | Mechanism: Updates the starting page for Lua scripting with a new design. | Purpose: Provides a better user experience for developers learning to script in Roblox.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 16390d61c6794f018273901c0ebb77a42fbb0854 to 39e7cb3a77654caad8af0fc17bfe2316176ae0b9 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 18:47:25 to 01/22/2026 18:49:13 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 16390d61c6794f018273901c0ebb77a42fbb0854 to 39e7cb3a77654caad8af0fc17bfe2316176ae0b9 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 18:47:25 to 01/22/2026 18:49:13 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## ebcda5baf - 2026-01-22 12:48:58 -0600 - 01/22/2026 12:48:57
Added in Camera/UI:
- FFlagLuaStartPageBuilderIcons2_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T18:46:10 | Mechanism: Enables new icons for the page builder in Lua scripts. | Purpose: Improves the visual experience for developers using the page builder.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 99b76cdc04f4e61a2a811b4cd33128df804100fd to 16390d61c6794f018273901c0ebb77a42fbb0854 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 18:41:49 to 01/22/2026 18:47:25 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 99b76cdc04f4e61a2a811b4cd33128df804100fd to 16390d61c6794f018273901c0ebb77a42fbb0854 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 18:41:49 to 01/22/2026 18:47:25 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 2ef81d800 - 2026-01-22 12:44:28 -0600 - 01/22/2026 12:44:28
Added in Other:
- FFlagEnableEventsRedesign3 = True | Mechanism: Activates a new design for event features in the platform. | Purpose: Enhances the overall look and functionality of events for players.
- FFlagEventUseBottomButtonByDefault = True | Mechanism: Sets the bottom button as the default action for events. | Purpose: Simplifies user interactions by making the most common action easier to access.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from a68f78d41ff3ac997c082cc0f9e4c78afe18f048 to 99b76cdc04f4e61a2a811b4cd33128df804100fd | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 18:40:40 to 01/22/2026 18:41:49 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FFlagVideoEnableHevcEncode2 changed from True to False | Mechanism: Enables HEVC encoding for video uploads, improving compression efficiency. | Purpose: Allows players to upload higher quality videos with smaller file sizes.
- FStringFlagRepoGitHashFastString changed from a68f78d41ff3ac997c082cc0f9e4c78afe18f048 to 99b76cdc04f4e61a2a811b4cd33128df804100fd | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 18:40:40 to 01/22/2026 18:41:49 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagEnableEventsRedesign3_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;369613356;2026-01-22T17:36:07) | Mechanism: Redesigns the event system for better functionality and user experience. | Purpose: Improves how players interact with events, making them more engaging and easier to use.
- FFlagEventUseBottomButtonByDefault_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;369613356;2026-01-22T17:36:07) | Mechanism: Sets the bottom button as the default action for events. | Purpose: Streamlines interactions for players, making it easier to participate in events.
- FFlagVideoEnableHevcEncode2_Staged removed (was false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T17:40:17) | Mechanism: Enables HEVC video encoding for better compression. | Purpose: Provides higher quality video streaming with less data usage for players.

## e5ba483d5 - 2026-01-22 12:42:12 -0600 - 01/22/2026 12:42:12
Added in Body:
- FFlagLcFmdIgnoreEditableBodyPart_Staged = true;SteadyState;10;30;Revert;2026-01-22T18:39:58 | Mechanism: Modifies how editable body parts are treated in the game engine. | Purpose: Allows for better customization options without affecting gameplay mechanics.
Added in Other:
- FFlagWrapDeformerContextOutputFileMeshData7_Staged = true;SteadyState;10;30;Revert;2026-01-22T18:39:58 | Mechanism: Improves the way mesh data is processed and handled in the game engine. | Purpose: Enhances the performance and quality of 3D models in games.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 1d833ed8af325742e6dade2ca7304a0bd952d740 to a68f78d41ff3ac997c082cc0f9e4c78afe18f048 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 18:36:50 to 01/22/2026 18:40:40 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 1d833ed8af325742e6dade2ca7304a0bd952d740 to a68f78d41ff3ac997c082cc0f9e4c78afe18f048 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 18:36:50 to 01/22/2026 18:40:40 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 06ae9e5c4 - 2026-01-22 12:37:41 -0600 - 01/22/2026 12:37:41
Changed in Other:
- DFFlagEnableSystrayBackgroundAppUpdate changed from True to False | Mechanism: Allows the app to update in the background via the system tray. | Purpose: Keeps the Roblox app up-to-date without interrupting the player's experience.
- DFStringFlagRepoGitHashDynamicString changed from b2e28cd41b58cde69327142d6eecc99e32e8aae7 to 1d833ed8af325742e6dade2ca7304a0bd952d740 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 18:31:04 to 01/22/2026 18:36:50 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from b2e28cd41b58cde69327142d6eecc99e32e8aae7 to 1d833ed8af325742e6dade2ca7304a0bd952d740 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 18:31:04 to 01/22/2026 18:36:50 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- DFFlagEnableSystrayBackgroundAppUpdate_Staged removed (was false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T17:31:28) | Mechanism: Allows the app to update in the background via the system tray. | Purpose: Keeps the app up to date without interrupting the player's experience.
- FFlagIASModifierKeys_Staged removed (was true;SteadyState;10;30;Revert;2026-01-22T18:02:47) | Mechanism: Enables specific key combinations for input actions. | Purpose: Allows players to use custom key shortcuts for better control.

## 8ea8c7373 - 2026-01-22 12:33:12 -0600 - 01/22/2026 12:33:11
Added in Other:
- FFlagRemoveBackendAdsDestructor_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;338665152;2026-01-22T18:29:52 | Mechanism: Eliminates a component that was responsible for managing backend ads. | Purpose: Reduces clutter and potential issues related to ads, leading to a smoother gameplay experience.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 90f0442dbe0ce7359622f315834bc8e5923440d2 to b2e28cd41b58cde69327142d6eecc99e32e8aae7 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 18:21:38 to 01/22/2026 18:31:04 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 90f0442dbe0ce7359622f315834bc8e5923440d2 to b2e28cd41b58cde69327142d6eecc99e32e8aae7 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 18:21:38 to 01/22/2026 18:31:04 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## ee95caa7f - 2026-01-22 12:24:16 -0600 - 01/22/2026 12:24:16
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from ae4e65e5ffe3f7a501979d5551e70b72fb7cc6ef to 90f0442dbe0ce7359622f315834bc8e5923440d2 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 18:18:55 to 01/22/2026 18:21:38 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FFlagTypeBandwidthMetrics changed from True to False | Mechanism: Tracks and analyzes data usage for better performance. | Purpose: Helps players experience smoother gameplay by optimizing data flow.
- FStringFlagRepoGitHashFastString changed from ae4e65e5ffe3f7a501979d5551e70b72fb7cc6ef to 90f0442dbe0ce7359622f315834bc8e5923440d2 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 18:18:55 to 01/22/2026 18:21:38 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagTypeBandwidthMetrics_Staged removed (was false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T17:16:45) | Mechanism: Tracks and analyzes the amount of data used by different types of content. | Purpose: Helps optimize game performance and loading times for players.

## f8783c13e - 2026-01-22 12:19:45 -0600 - 01/22/2026 12:19:44
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from d83e31158bd9d914080a9ff2aae058d28f865a7f to ae4e65e5ffe3f7a501979d5551e70b72fb7cc6ef | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 18:12:06 to 01/22/2026 18:18:55 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from d83e31158bd9d914080a9ff2aae058d28f865a7f to ae4e65e5ffe3f7a501979d5551e70b72fb7cc6ef | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 18:12:06 to 01/22/2026 18:18:55 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 0d076a0c5 - 2026-01-22 12:12:59 -0600 - 01/22/2026 12:12:59
Added in Input:
- FFlagTouchEventCodeRefactor_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T18:10:44 | Mechanism: Improves the code handling touch events. | Purpose: Enhances responsiveness and accuracy of touch controls for players.
Added in Other:
- FStringSystrayExperimentBucketSettings2 = v4-15-29 | Mechanism: Controls settings for user interface experiments in the system tray. | Purpose: Improves user experience by testing new interface features.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from b254c51bcdf3e62a5bdc567e85e91d3988ebc5ec to d83e31158bd9d914080a9ff2aae058d28f865a7f | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 18:09:45 to 01/22/2026 18:12:06 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from b254c51bcdf3e62a5bdc567e85e91d3988ebc5ec to d83e31158bd9d914080a9ff2aae058d28f865a7f | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 18:09:45 to 01/22/2026 18:12:06 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FStringSystrayExperimentBucketSettings2_Staged removed (was v4-15-29;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T17:06:00) | Mechanism: Adjusts settings for the experimental system tray features. | Purpose: Optimizes the testing of new features, improving user experience during trials.

## 6174cab61 - 2026-01-22 12:10:41 -0600 - 01/22/2026 12:10:41
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from cf63edf31c6538ab06e284a85a994e89519b031e to b254c51bcdf3e62a5bdc567e85e91d3988ebc5ec | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 18:07:14 to 01/22/2026 18:09:45 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from cf63edf31c6538ab06e284a85a994e89519b031e to b254c51bcdf3e62a5bdc567e85e91d3988ebc5ec | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 18:07:14 to 01/22/2026 18:09:45 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## f50423c8d - 2026-01-22 12:08:24 -0600 - 01/22/2026 12:08:24
Added in Other:
- FFlagStudioUpdateShutdownButton_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;73257166;2026-01-22T18:04:16 | Mechanism: Adds a button in Roblox Studio to easily shut down the application after updates. | Purpose: Makes it more convenient for developers to manage their workflow by quickly closing the Studio after updates.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 42c6b74b115af8ee5fb158bffd2e84af9356b61b to cf63edf31c6538ab06e284a85a994e89519b031e | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 18:03:44 to 01/22/2026 18:07:14 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 42c6b74b115af8ee5fb158bffd2e84af9356b61b to cf63edf31c6538ab06e284a85a994e89519b031e | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 18:03:44 to 01/22/2026 18:07:14 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 4e03f4d64 - 2026-01-22 12:06:07 -0600 - 01/22/2026 12:06:07
Added in Other:
- FFlagIASModifierKeys_Staged = true;SteadyState;10;30;Revert;2026-01-22T18:02:47 | Mechanism: Enables specific key combinations for input actions. | Purpose: Allows players to use custom key shortcuts for better control.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from d554fdb811a197a50a59af94d5caef18587fad50 to 42c6b74b115af8ee5fb158bffd2e84af9356b61b | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 18:01:56 to 01/22/2026 18:03:44 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from d554fdb811a197a50a59af94d5caef18587fad50 to 42c6b74b115af8ee5fb158bffd2e84af9356b61b | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 18:01:56 to 01/22/2026 18:03:44 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 2dde42668 - 2026-01-22 12:03:50 -0600 - 01/22/2026 12:03:50
Added in Graphics:
- FFlagRefactorTexturePackManagement2_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T18:00:34 | Mechanism: Updates the system for managing texture packs in games. | Purpose: Makes it easier for developers to use and manage textures, improving game visuals.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from cf02547b5e5ab4432e40541c66a5c4edaba82eee to d554fdb811a197a50a59af94d5caef18587fad50 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 17:53:10 to 01/22/2026 18:01:56 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from cf02547b5e5ab4432e40541c66a5c4edaba82eee to d554fdb811a197a50a59af94d5caef18587fad50 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 17:53:10 to 01/22/2026 18:01:56 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 9bbc9f177 - 2026-01-22 11:54:58 -0600 - 01/22/2026 11:54:58
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 192e2bd0692a5f0c86f55b2d049ea37564186fc9 to cf02547b5e5ab4432e40541c66a5c4edaba82eee | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 17:51:59 to 01/22/2026 17:53:10 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 192e2bd0692a5f0c86f55b2d049ea37564186fc9 to cf02547b5e5ab4432e40541c66a5c4edaba82eee | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 17:51:59 to 01/22/2026 17:53:10 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 4f200b859 - 2026-01-22 11:52:43 -0600 - 01/22/2026 11:52:43
Added in Camera/UI:
- FIntStudioMenuOpenCooldownMillis_Staged = 200;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T17:51:18 | Mechanism: Introduces a cooldown period for opening the studio menu. | Purpose: Prevents accidental menu openings, making it easier for developers to work.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from ae2107f0fada170476f82e301372df67187c050b to 192e2bd0692a5f0c86f55b2d049ea37564186fc9 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 17:43:40 to 01/22/2026 17:51:59 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from ae2107f0fada170476f82e301372df67187c050b to 192e2bd0692a5f0c86f55b2d049ea37564186fc9 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 17:43:40 to 01/22/2026 17:51:59 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## f924b849b - 2026-01-22 11:46:01 -0600 - 01/22/2026 11:46:01
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 4d660fcec4a807c05a2f293304344b957ddbcb45 to ae2107f0fada170476f82e301372df67187c050b | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 17:40:57 to 01/22/2026 17:43:40 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 4d660fcec4a807c05a2f293304344b957ddbcb45 to ae2107f0fada170476f82e301372df67187c050b | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 17:40:57 to 01/22/2026 17:43:40 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## d14febd03 - 2026-01-22 11:41:29 -0600 - 01/22/2026 11:41:29
Added in Other:
- FFlagVideoEnableHevcEncode2_Staged = false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T17:40:17 | Mechanism: Enables HEVC video encoding for better compression. | Purpose: Provides higher quality video streaming with less data usage for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 6c5aa2f8db28e33e0bbf9790cd9e29f684a5ae18 to 4d660fcec4a807c05a2f293304344b957ddbcb45 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 17:36:58 to 01/22/2026 17:40:57 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 6c5aa2f8db28e33e0bbf9790cd9e29f684a5ae18 to 4d660fcec4a807c05a2f293304344b957ddbcb45 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 17:36:58 to 01/22/2026 17:40:57 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 6f26013ee - 2026-01-22 11:39:14 -0600 - 01/22/2026 11:39:14
Added in Other:
- FFlagEnableEventsRedesign3_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;369613356;2026-01-22T17:36:07 | Mechanism: Redesigns the event system for better functionality and user experience. | Purpose: Improves how players interact with events, making them more engaging and easier to use.
- FFlagEventUseBottomButtonByDefault_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;369613356;2026-01-22T17:36:07 | Mechanism: Sets the bottom button as the default action for events. | Purpose: Streamlines interactions for players, making it easier to participate in events.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from d64bf1966238b28d1b3adc7593717a3f5befbda5 to 6c5aa2f8db28e33e0bbf9790cd9e29f684a5ae18 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 17:34:01 to 01/22/2026 17:36:58 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from d64bf1966238b28d1b3adc7593717a3f5befbda5 to 6c5aa2f8db28e33e0bbf9790cd9e29f684a5ae18 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 17:34:01 to 01/22/2026 17:36:58 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## dde9dc688 - 2026-01-22 11:34:42 -0600 - 01/22/2026 11:34:42
Added in Other:
- DFFlagEnableSystrayBackgroundAppUpdate_Staged = false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T17:31:28 | Mechanism: Allows the app to update in the background via the system tray. | Purpose: Keeps the app up to date without interrupting the player's experience.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from eb47a67a1ae8ae37129116c14e4a137d42562f9e to d64bf1966238b28d1b3adc7593717a3f5befbda5 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 17:17:31 to 01/22/2026 17:34:01 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from eb47a67a1ae8ae37129116c14e4a137d42562f9e to d64bf1966238b28d1b3adc7593717a3f5befbda5 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 17:17:31 to 01/22/2026 17:34:01 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagVideoEnableHevcEncode2_Staged removed (was false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T17:15:23) | Mechanism: Enables HEVC video encoding for better compression. | Purpose: Provides higher quality video streaming with less data usage for players.

## 4f209e52a - 2026-01-22 11:18:54 -0600 - 01/22/2026 11:18:54
Added in Other:
- FFlagTypeBandwidthMetrics_Staged = false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T17:16:45 | Mechanism: Tracks and analyzes the amount of data used by different types of content. | Purpose: Helps optimize game performance and loading times for players.
- FFlagUseBindingForUnreadChat_IXP = 1;InExperience.Performance;InExperience.Performance.UnreadChat.Binding;63430395;flagbank | Mechanism: Uses a binding system to track unread chat messages. | Purpose: Helps players easily see which chat messages they haven't read yet.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from e59790e855970c17f572472792cab50bc9f746b2 to eb47a67a1ae8ae37129116c14e4a137d42562f9e | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 17:16:07 to 01/22/2026 17:17:31 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from e59790e855970c17f572472792cab50bc9f746b2 to eb47a67a1ae8ae37129116c14e4a137d42562f9e | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 17:16:07 to 01/22/2026 17:17:31 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 06303e521 - 2026-01-22 11:16:38 -0600 - 01/22/2026 11:16:38
Added in Other:
- FFlagVideoEnableHevcEncode2_Staged = false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T17:15:23 | Mechanism: Enables HEVC video encoding for better compression. | Purpose: Provides higher quality video streaming with less data usage for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from b7f5885ea3d3a9aa4e94d5be4254fbe9da34e777 to e59790e855970c17f572472792cab50bc9f746b2 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 17:11:43 to 01/22/2026 17:16:07 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from b7f5885ea3d3a9aa4e94d5be4254fbe9da34e777 to e59790e855970c17f572472792cab50bc9f746b2 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 17:11:43 to 01/22/2026 17:16:07 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## b4c01d363 - 2026-01-22 11:12:07 -0600 - 01/22/2026 11:12:07
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 59a1aec37061a0d2d0d8e2a69343539dd12d4dd1 to b7f5885ea3d3a9aa4e94d5be4254fbe9da34e777 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 17:09:10 to 01/22/2026 17:11:43 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 59a1aec37061a0d2d0d8e2a69343539dd12d4dd1 to b7f5885ea3d3a9aa4e94d5be4254fbe9da34e777 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 17:09:10 to 01/22/2026 17:11:43 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 41bb9495a - 2026-01-22 11:09:46 -0600 - 01/22/2026 11:09:46
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 3ed4d0fa15f3b6799400356708fa0ed58e3bff49 to 59a1aec37061a0d2d0d8e2a69343539dd12d4dd1 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 17:06:41 to 01/22/2026 17:09:10 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 3ed4d0fa15f3b6799400356708fa0ed58e3bff49 to 59a1aec37061a0d2d0d8e2a69343539dd12d4dd1 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 17:06:41 to 01/22/2026 17:09:10 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## abb3f1eb4 - 2026-01-22 11:07:28 -0600 - 01/22/2026 11:07:27
Added in Other:
- FStringSystrayExperimentBucketSettings2_Staged = v4-15-29;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T17:06:00 | Mechanism: Adjusts settings for the experimental system tray features. | Purpose: Optimizes the testing of new features, improving user experience during trials.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from bde6e3ca30e28dbe4a280ba1bf2fc273edc0062c to 3ed4d0fa15f3b6799400356708fa0ed58e3bff49 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 01:51:32 to 01/22/2026 17:06:41 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from bde6e3ca30e28dbe4a280ba1bf2fc273edc0062c to 3ed4d0fa15f3b6799400356708fa0ed58e3bff49 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 01:51:32 to 01/22/2026 17:06:41 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 170e26929 - 2026-01-21 19:52:46 -0600 - 01/21/2026 19:52:46
Added in Other:
- FFlagInExperienceRequestProfileSettings = True | Mechanism: Allows games to request access to player profile settings directly within the experience. | Purpose: Enables more personalized experiences by accessing player settings seamlessly.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 4fc2dc7b50d91aef4b82cb35623e2d628208687a to bde6e3ca30e28dbe4a280ba1bf2fc273edc0062c | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 01:31:40 to 01/22/2026 01:51:32 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 4fc2dc7b50d91aef4b82cb35623e2d628208687a to bde6e3ca30e28dbe4a280ba1bf2fc273edc0062c | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 01:31:40 to 01/22/2026 01:51:32 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagInExperienceRequestProfileSettings_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T00:48:55) | Mechanism: Enables new profile settings to be requested within experiences. | Purpose: Allows players to access and modify their profile settings more easily.

## bce950d55 - 2026-01-21 19:32:54 -0600 - 01/21/2026 19:32:53
Added in Other:
- FFlagEnableHttpStreamingForMsxml = True | Mechanism: Enables HTTP streaming capabilities for XML data processing. | Purpose: Allows for faster and more efficient data loading, improving game performance and responsiveness.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from c3af12d56b29e32441da8b97e9b0fe0a74aeeb30 to 4fc2dc7b50d91aef4b82cb35623e2d628208687a | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 01:11:45 to 01/22/2026 01:31:40 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from c3af12d56b29e32441da8b97e9b0fe0a74aeeb30 to 4fc2dc7b50d91aef4b82cb35623e2d628208687a | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 01:11:45 to 01/22/2026 01:31:40 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagEnableHttpStreamingForMsxml_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T00:30:04) | Mechanism: Enables streaming of HTTP content using a specific XML format. | Purpose: Allows for faster loading of game assets from the web, improving gameplay experience.

## 787a760b1 - 2026-01-21 19:12:53 -0600 - 01/21/2026 19:12:53
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 7f04efbeb9e18b3d49336d03c05d56fd39696f2a to c3af12d56b29e32441da8b97e9b0fe0a74aeeb30 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 01:02:29 to 01/22/2026 01:11:45 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 7f04efbeb9e18b3d49336d03c05d56fd39696f2a to c3af12d56b29e32441da8b97e9b0fe0a74aeeb30 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 01:02:29 to 01/22/2026 01:11:45 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 417161f1e - 2026-01-21 19:04:01 -0600 - 01/21/2026 19:04:01
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from d276764fc7da76e83e0f7ceabc34d99f92f39aee to 7f04efbeb9e18b3d49336d03c05d56fd39696f2a | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 00:56:38 to 01/22/2026 01:02:29 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from d276764fc7da76e83e0f7ceabc34d99f92f39aee to 7f04efbeb9e18b3d49336d03c05d56fd39696f2a | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 00:56:38 to 01/22/2026 01:02:29 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Changed in Camera/UI:
- FFlagAvatarAnimationCameraZoom changed from True to False | Mechanism: Adjusts camera zoom based on avatar animations. | Purpose: Improves the viewing experience by allowing players to see their avatars better during animations.
Removed in Camera/UI:
- FFlagAvatarAnimationCameraZoom_Staged removed (was false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;1122964870;2026-01-21T23:59:49) | Mechanism: Adjusts the camera zoom level during avatar animations for better visibility. | Purpose: Provides players with a clearer view of their avatars during animations, improving gameplay experience.

## 99ada3ad5 - 2026-01-21 18:57:18 -0600 - 01/21/2026 18:57:17
Added in Network:
- DFFlagFixTeleportToReservedServerHang = True | Mechanism: N/A (invalid) | Purpose: N/A (invalid)
- DFFlagFixTeleportToReservedServerPlayerHang = True | Mechanism: Fixes an issue where players get stuck when teleporting to reserved servers. | Purpose: Ensures smoother teleportation for players, reducing frustration.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 41587942bbf4e6f9726bf23ffbb3e2059c6d48f9 to d276764fc7da76e83e0f7ceabc34d99f92f39aee | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 00:51:59 to 01/22/2026 00:56:38 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 41587942bbf4e6f9726bf23ffbb3e2059c6d48f9 to d276764fc7da76e83e0f7ceabc34d99f92f39aee | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 00:51:59 to 01/22/2026 00:56:38 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Network:
- DFFlagFixTeleportToReservedServerHang_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:54:42) | Mechanism: Addresses a delay when players try to move to a reserved game server. | Purpose: Reduces waiting time for players when joining specific game servers.
- DFFlagFixTeleportToReservedServerPlayerHang_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:52:43) | Mechanism: Fixes an issue where players would get stuck when teleporting to reserved servers. | Purpose: Ensures players can teleport without delays or getting stuck, enhancing gameplay flow.

## 67a02bda4 - 2026-01-21 18:52:43 -0600 - 01/21/2026 18:52:43
Added in Other:
- FFlagInExperienceRequestProfileSettings_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T00:48:55 | Mechanism: Enables new profile settings to be requested within experiences. | Purpose: Allows players to access and modify their profile settings more easily.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 2e25b071909ec16fd2698830c6ecf09064b44fa1 to 41587942bbf4e6f9726bf23ffbb3e2059c6d48f9 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 00:46:53 to 01/22/2026 00:51:59 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 2e25b071909ec16fd2698830c6ecf09064b44fa1 to 41587942bbf4e6f9726bf23ffbb3e2059c6d48f9 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 00:46:53 to 01/22/2026 00:51:59 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 29521f583 - 2026-01-21 18:48:09 -0600 - 01/21/2026 18:48:09
Added in Camera/UI:
- FFlagFixMoreSubMenuTitleFlash = True | Mechanism: Addresses visual issues with submenu titles flashing. | Purpose: Creates a smoother and more visually appealing interface for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 5be446d544a53871d3ac2a3a40e67d412b606ccc to 2e25b071909ec16fd2698830c6ecf09064b44fa1 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 00:30:56 to 01/22/2026 00:46:53 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 5be446d544a53871d3ac2a3a40e67d412b606ccc to 2e25b071909ec16fd2698830c6ecf09064b44fa1 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 00:30:56 to 01/22/2026 00:46:53 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Camera/UI:
- FFlagFixMoreSubMenuTitleFlash_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:42:58) | Mechanism: Addresses issues with flashing titles in submenus by refining the display logic. | Purpose: Enhances the visual experience for players by reducing distracting flashes in menus.

## becf90185 - 2026-01-21 18:32:41 -0600 - 01/21/2026 18:32:41
Added in Other:
- FFlagEnableHttpStreamingForMsxml_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T00:30:04 | Mechanism: Enables streaming of HTTP content using a specific XML format. | Purpose: Allows for faster loading of game assets from the web, improving gameplay experience.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from d156c1cedb8791c6246ef9dd5e45c16d87bf80c5 to 5be446d544a53871d3ac2a3a40e67d412b606ccc | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 00:27:18 to 01/22/2026 00:30:56 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from d156c1cedb8791c6246ef9dd5e45c16d87bf80c5 to 5be446d544a53871d3ac2a3a40e67d412b606ccc | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 00:27:18 to 01/22/2026 00:30:56 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## d4217dd81 - 2026-01-21 18:28:12 -0600 - 01/21/2026 18:28:12
Added in Other:
- FFlagEnableRewardedAdFormatExperiment = True | Mechanism: Tests a new format for showing rewarded ads to players. | Purpose: Offers players more engaging ways to earn rewards through ads.
- FFlagPassAdUnitToNativeAndroid = True | Mechanism: Sends ad unit information to the Android app for better ad handling. | Purpose: Improves ad display and performance on Android devices.
- FFlagSendRewardedVideoExperimentVariantAndAdUnitIdToNative2 = True | Mechanism: Sends data about video ads and their versions to the app. | Purpose: Enhances the ad experience by providing tailored video rewards.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from da26789b12b7bd8376a537646b7381436a1b8728 to d156c1cedb8791c6246ef9dd5e45c16d87bf80c5 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 00:21:56 to 01/22/2026 00:27:18 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from da26789b12b7bd8376a537646b7381436a1b8728 to d156c1cedb8791c6246ef9dd5e45c16d87bf80c5 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 00:21:56 to 01/22/2026 00:27:18 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagEnableRewardedAdFormatExperiment_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;2028022506;2026-01-21T23:21:48) | Mechanism: Enables a new format for displaying rewarded ads in games. | Purpose: Players can earn rewards by watching ads, enhancing their gaming experience.
- FFlagPassAdUnitToNativeAndroid_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;2028022506;2026-01-21T23:21:48) | Mechanism: Sends ad unit information directly to the Android app. | Purpose: Improves ad targeting and relevance for players using the Android app.
- FFlagSendRewardedVideoExperimentVariantAndAdUnitIdToNative2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;2028022506;2026-01-21T23:21:48) | Mechanism: Sends specific data about video ads to the native app for better tracking. | Purpose: Enhances the experience and rewards from watching video ads.

## 4c6a2d5a3 - 2026-01-21 18:23:40 -0600 - 01/21/2026 18:23:40
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from ead87777d27124b06e6f5be6d3783dd1015bdac5 to da26789b12b7bd8376a537646b7381436a1b8728 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 00:17:28 to 01/22/2026 00:21:56 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from ead87777d27124b06e6f5be6d3783dd1015bdac5 to da26789b12b7bd8376a537646b7381436a1b8728 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 00:17:28 to 01/22/2026 00:21:56 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 9a8415808 - 2026-01-21 18:19:12 -0600 - 01/21/2026 18:19:12
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from e304719ff0f58c7b2dedbc0d7b2acd819833492f to ead87777d27124b06e6f5be6d3783dd1015bdac5 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 00:12:07 to 01/22/2026 00:17:28 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FFlagExplorerHeartbeatTelemetry changed from True to False | Mechanism: Collects data on the performance and usage of the Explorer tool in Roblox Studio. | Purpose: Helps improve the Explorer tool by understanding how players use it.
- FStringFlagRepoGitHashFastString changed from e304719ff0f58c7b2dedbc0d7b2acd819833492f to ead87777d27124b06e6f5be6d3783dd1015bdac5 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 00:12:07 to 01/22/2026 00:17:28 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagExplorerHeartbeatTelemetry_Staged removed (was false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:11:01) | Mechanism: Collects data on the performance of the Explorer tool in real-time. | Purpose: Helps improve the Explorer tool's performance and reliability for developers.

## 3808f1a95 - 2026-01-21 18:14:42 -0600 - 01/21/2026 18:14:42
Added in Other:
- DFFlagMathUseNewReflection2 = True | Mechanism: Switches to a new method for mathematical calculations in the game engine. | Purpose: Increases accuracy and performance of calculations, leading to smoother gameplay.
- DFFlagSimCSG3EnableNewAPIPluginUse2 = True | Mechanism: Allows the use of a new API for plugins related to CSG (Constructive Solid Geometry) in simulations. | Purpose: Gives developers more tools to create complex shapes, enhancing game design.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 7e358cdff52250f1285194dbaf7dbecc476a3683 to e304719ff0f58c7b2dedbc0d7b2acd819833492f | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 00:07:42 to 01/22/2026 00:12:07 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 7e358cdff52250f1285194dbaf7dbecc476a3683 to e304719ff0f58c7b2dedbc0d7b2acd819833492f | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 00:07:42 to 01/22/2026 00:12:07 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- DFFlagMathUseNewReflection2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:09:58) | Mechanism: Enables a new method for mathematical calculations in the game engine. | Purpose: Improves the accuracy and performance of math-related functions for smoother gameplay.
- DFFlagSimCSG3EnableNewAPIPluginUse2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:09:06) | Mechanism: Enables the use of a new API for construction in Roblox. | Purpose: Allows developers to create more complex and efficient models in their games.

## 9a8352c74 - 2026-01-21 18:10:11 -0600 - 01/21/2026 18:10:11
Added in Other:
- FFlagCaptureServiceEnableTakeCaptureApi2 = True | Mechanism: Activates a new API for capturing in-game screenshots. | Purpose: Allows players to easily take and share screenshots of their gameplay.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 055fb5e03ba54e044a347f2748a92740e58495a6 to 7e358cdff52250f1285194dbaf7dbecc476a3683 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 00:06:13 to 01/22/2026 00:07:42 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 055fb5e03ba54e044a347f2748a92740e58495a6 to 7e358cdff52250f1285194dbaf7dbecc476a3683 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 00:06:13 to 01/22/2026 00:07:42 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagCaptureServiceEnableTakeCaptureApi2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:02:54) | Mechanism: Enables a new API for capturing game states. | Purpose: Allows players to take better snapshots of their game progress.

## 9ba543334 - 2026-01-21 18:07:56 -0600 - 01/21/2026 18:07:55
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 56a49c980d9a6af659dc2fb741ff3c0ef3d7f645 to 055fb5e03ba54e044a347f2748a92740e58495a6 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 00:01:03 to 01/22/2026 00:06:13 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 56a49c980d9a6af659dc2fb741ff3c0ef3d7f645 to 055fb5e03ba54e044a347f2748a92740e58495a6 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/22/2026 00:01:03 to 01/22/2026 00:06:13 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 88d1f3e76 - 2026-01-21 18:03:17 -0600 - 01/21/2026 18:03:17
Added in Camera/UI:
- FFlagAvatarAnimationCameraZoom_Staged = false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;1122964870;2026-01-21T23:59:49 | Mechanism: Adjusts the camera zoom level during avatar animations for better visibility. | Purpose: Provides players with a clearer view of their avatars during animations, improving gameplay experience.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from e58337c29e49e81e38600507b08d02e584ee6709 to 56a49c980d9a6af659dc2fb741ff3c0ef3d7f645 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 23:57:21 to 01/22/2026 00:01:03 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from e58337c29e49e81e38600507b08d02e584ee6709 to 56a49c980d9a6af659dc2fb741ff3c0ef3d7f645 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 23:57:21 to 01/22/2026 00:01:03 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 507b92d4c - 2026-01-21 17:58:47 -0600 - 01/21/2026 17:58:47
Added in Other:
- DFFlagEnableSystrayExpEnrollment = True | Mechanism: Enables a system tray for managing experimental features. | Purpose: Allows players to easily access and enroll in new features being tested.
- FFlagAmrFixCustomizeGroups = True | Mechanism: Fixes issues with customizing groups in the AMR system. | Purpose: Enhances group management features for players, making it easier to organize and customize groups.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from c2f964affed08f6cafdcb745960403916b39b973 to e58337c29e49e81e38600507b08d02e584ee6709 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 23:55:36 to 01/21/2026 23:57:21 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from c2f964affed08f6cafdcb745960403916b39b973 to e58337c29e49e81e38600507b08d02e584ee6709 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 23:55:36 to 01/21/2026 23:57:21 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- DFFlagEnableSystrayExpEnrollment_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:53:30) | Mechanism: Enables a system tray for user experience enrollment. | Purpose: Allows players to easily opt into new features and experiences.
- FFlagAmrFixCustomizeGroups_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;1964796395;2026-01-21T22:51:36) | Mechanism: Fixes issues with customizing group settings in the avatar system. | Purpose: Allows players to better customize their groups without errors.

## c6d0101a6 - 2026-01-21 17:56:31 -0600 - 01/21/2026 17:56:31
Added in Network:
- DFFlagFixTeleportToReservedServerHang_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:54:42 | Mechanism: Addresses a delay when players try to move to a reserved game server. | Purpose: Reduces waiting time for players when joining specific game servers.
- DFFlagFixTeleportToReservedServerPlayerHang_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:52:43 | Mechanism: Fixes an issue where players would get stuck when teleporting to reserved servers. | Purpose: Ensures players can teleport without delays or getting stuck, enhancing gameplay flow.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from a6bc744c1a36205210d284808360bee295b541f6 to c2f964affed08f6cafdcb745960403916b39b973 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 23:51:42 to 01/21/2026 23:55:36 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from a6bc744c1a36205210d284808360bee295b541f6 to c2f964affed08f6cafdcb745960403916b39b973 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 23:51:42 to 01/21/2026 23:55:36 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## bbc7fd9a9 - 2026-01-21 17:54:15 -0600 - 01/21/2026 17:54:14
Added in Other:
- DFFlagEnableSystrayBackgroundAppUpdate = True | Mechanism: Allows the app to update in the background via the system tray. | Purpose: Keeps the Roblox app up-to-date without interrupting the player's experience.
- DFIntSystrayEventsThrottleHundredthsPercent = 10000 | Mechanism: Regulates the frequency of events sent to the system tray. | Purpose: Reduces clutter and improves performance by managing notifications.
- FFlagSystemTrayDeviceSettings2 = True | Mechanism: Updates the system tray settings for device management. | Purpose: Provides players with easier access to device settings and configurations.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from cdd8a37756a41e5713345a5bf6d3874d9ffe3305 to a6bc744c1a36205210d284808360bee295b541f6 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 23:51:04 to 01/21/2026 23:51:42 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from cdd8a37756a41e5713345a5bf6d3874d9ffe3305 to a6bc744c1a36205210d284808360bee295b541f6 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 23:51:04 to 01/21/2026 23:51:42 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- DFFlagEnableSystrayBackgroundAppUpdate_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:50:10) | Mechanism: Allows the app to update in the background via the system tray. | Purpose: Keeps the app up to date without interrupting the player's experience.
- DFIntSystrayEventsThrottleHundredthsPercent_Staged removed (was 10000;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:46:36) | Mechanism: Adjusts the frequency of system tray event notifications. | Purpose: Reduces notification clutter, allowing players to focus on their games without distractions.
- FFlagSystemTrayDeviceSettings2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:47:38) | Mechanism: Implements new device settings accessible from the system tray. | Purpose: Provides players with easier access to device settings for a better gaming experience.

## 81b588b9d - 2026-01-21 17:51:57 -0600 - 01/21/2026 17:51:57
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from f5b99c00682fd74ee980739e7d697cb0571001f1 to cdd8a37756a41e5713345a5bf6d3874d9ffe3305 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 23:47:15 to 01/21/2026 23:51:04 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from f5b99c00682fd74ee980739e7d697cb0571001f1 to cdd8a37756a41e5713345a5bf6d3874d9ffe3305 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 23:47:15 to 01/21/2026 23:51:04 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 2624d2bbc - 2026-01-21 17:49:42 -0600 - 01/21/2026 17:49:41
Added in Other:
- DFFlagRemoveTrayUserAgentKeyword = True | Mechanism: Eliminates a specific keyword from the user agent string sent to servers. | Purpose: Enhances privacy and reduces unnecessary data sent to servers.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from e93f0d569677281931d803b5445b009020f11433 to f5b99c00682fd74ee980739e7d697cb0571001f1 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 23:44:49 to 01/21/2026 23:47:15 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from e93f0d569677281931d803b5445b009020f11433 to f5b99c00682fd74ee980739e7d697cb0571001f1 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 23:44:49 to 01/21/2026 23:47:15 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- DFFlagRemoveTrayUserAgentKeyword_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:45:24) | Mechanism: Removes specific keywords from the user agent string sent to servers. | Purpose: Enhances privacy and security for players by not revealing unnecessary information.

## 98b23afa2 - 2026-01-21 17:47:24 -0600 - 01/21/2026 17:47:24
Added in Camera/UI:
- FFlagFixMoreSubMenuTitleFlash_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:42:58 | Mechanism: Addresses issues with flashing titles in submenus by refining the display logic. | Purpose: Enhances the visual experience for players by reducing distracting flashes in menus.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 38a9fdf126a09509db576091ef227c2465294f96 to e93f0d569677281931d803b5445b009020f11433 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 23:27:10 to 01/21/2026 23:44:49 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 38a9fdf126a09509db576091ef227c2465294f96 to e93f0d569677281931d803b5445b009020f11433 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 23:27:10 to 01/21/2026 23:44:49 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 715b6d898 - 2026-01-21 17:29:42 -0600 - 01/21/2026 17:29:41
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from fe9d54586cddab42e8b0bd3e5e4ebf7cbb9bb506 to 38a9fdf126a09509db576091ef227c2465294f96 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 23:23:45 to 01/21/2026 23:27:10 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FFlagLuaAppGameTileWideVideoThumbnail changed from True to False | Mechanism: Enables wider video thumbnails for game tiles in the app. | Purpose: Provides a more visually appealing and engaging display of game videos.
- FStringFlagRepoGitHashFastString changed from fe9d54586cddab42e8b0bd3e5e4ebf7cbb9bb506 to 38a9fdf126a09509db576091ef227c2465294f96 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 23:23:45 to 01/21/2026 23:27:10 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagLuaAppGameTileWideVideoThumbnail_Staged removed (was false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:25:00) | Mechanism: Enables wider video thumbnails for game tiles in the app. | Purpose: Enhances visual appeal and engagement by showcasing game videos more prominently.

## 20d7cf1ef - 2026-01-21 17:25:10 -0600 - 01/21/2026 17:25:09
Added in Other:
- DFFlagUseCompletedRadiusFunc = True | Mechanism: Implements a new function to calculate distances more accurately. | Purpose: Improves gameplay by ensuring players interact with objects correctly based on their distance.
- FFlagEnableRewardedAdFormatExperiment_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;2028022506;2026-01-21T23:21:48 | Mechanism: Enables a new format for displaying rewarded ads in games. | Purpose: Players can earn rewards by watching ads, enhancing their gaming experience.
- FFlagPassAdUnitToNativeAndroid_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;2028022506;2026-01-21T23:21:48 | Mechanism: Sends ad unit information directly to the Android app. | Purpose: Improves ad targeting and relevance for players using the Android app.
- FFlagSendRewardedVideoExperimentVariantAndAdUnitIdToNative2_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;2028022506;2026-01-21T23:21:48 | Mechanism: Sends specific data about video ads to the native app for better tracking. | Purpose: Enhances the experience and rewards from watching video ads.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 335bc44fc6a4ba540416f7af5640246f50d78103 to fe9d54586cddab42e8b0bd3e5e4ebf7cbb9bb506 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 23:19:27 to 01/21/2026 23:23:45 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 335bc44fc6a4ba540416f7af5640246f50d78103 to fe9d54586cddab42e8b0bd3e5e4ebf7cbb9bb506 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 23:19:27 to 01/21/2026 23:23:45 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- DFFlagUseCompletedRadiusFunc_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:18:16) | Mechanism: Uses a new function for calculating radius in game physics. | Purpose: Enhances the accuracy of physics interactions in the game.

## 14a7e3774 - 2026-01-21 17:20:34 -0600 - 01/21/2026 17:20:34
Added in Other:
- DFFlagCLI184446 = True | Mechanism: Enables a specific command line interface feature for developers. | Purpose: Provides developers with better tools to manage and debug their games.
- FFlagAXScrollingListAutomaticCanvasSize = True | Mechanism: Automatically adjusts the size of scrolling lists in the UI. | Purpose: Makes user interfaces more responsive and easier to navigate.
Added in Camera/UI:
- FFlagAbuseReportMenuScreenshotReduceMotionFix = True | Mechanism: Reduces motion effects in the screenshot feature of the abuse report menu. | Purpose: Makes it easier for players to take clear screenshots when reporting issues.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 855cef1e5c6e58a94532a9782bfa6e589f62135f to 335bc44fc6a4ba540416f7af5640246f50d78103 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 23:12:33 to 01/21/2026 23:19:27 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 855cef1e5c6e58a94532a9782bfa6e589f62135f to 335bc44fc6a4ba540416f7af5640246f50d78103 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 23:12:33 to 01/21/2026 23:19:27 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- DFFlagCLI184446_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:12:37) | Mechanism: Implements a staged rollout of a command-line interface feature. | Purpose: Allows developers to test new features safely before full release.
- FFlagAXScrollingListAutomaticCanvasSize_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:11:33) | Mechanism: Automatically adjusts the size of scrolling lists based on content. | Purpose: Ensures that lists display correctly without unnecessary scrolling, enhancing usability.
Removed in Camera/UI:
- FFlagAbuseReportMenuScreenshotReduceMotionFix_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:13:20) | Mechanism: Reduces motion effects in the abuse report menu when taking screenshots. | Purpose: Makes it easier for players to capture and report issues without distractions.

## 7939ec87e - 2026-01-21 17:13:53 -0600 - 01/21/2026 17:13:53
Added in Other:
- DFFlagMathUseNewReflection2_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:09:58 | Mechanism: Enables a new method for mathematical calculations in the game engine. | Purpose: Improves the accuracy and performance of math-related functions for smoother gameplay.
- DFFlagSimCSG3EnableNewAPIPluginUse2_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:09:06 | Mechanism: Enables the use of a new API for construction in Roblox. | Purpose: Allows developers to create more complex and efficient models in their games.
- FFlagExplorerHeartbeatTelemetry_Staged = false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:11:01 | Mechanism: Collects data on the performance of the Explorer tool in real-time. | Purpose: Helps improve the Explorer tool's performance and reliability for developers.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 452e2b3eaf65f91dc1b08384d4f3ae96ae270294 to 855cef1e5c6e58a94532a9782bfa6e589f62135f | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 23:04:14 to 01/21/2026 23:12:33 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 452e2b3eaf65f91dc1b08384d4f3ae96ae270294 to 855cef1e5c6e58a94532a9782bfa6e589f62135f | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 23:04:14 to 01/21/2026 23:12:33 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 052a356c5 - 2026-01-21 17:04:54 -0600 - 01/21/2026 17:04:54
Added in Other:
- FFlagCaptureServiceEnableTakeCaptureApi2_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:02:54 | Mechanism: Enables a new API for capturing game states. | Purpose: Allows players to take better snapshots of their game progress.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from e4a41f124952825288dd2dc170cf89025f549da6 to 452e2b3eaf65f91dc1b08384d4f3ae96ae270294 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:55:53 to 01/21/2026 23:04:14 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from e4a41f124952825288dd2dc170cf89025f549da6 to 452e2b3eaf65f91dc1b08384d4f3ae96ae270294 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:55:53 to 01/21/2026 23:04:14 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## c6e0eac80 - 2026-01-21 16:58:13 -0600 - 01/21/2026 16:58:13
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 881b91a9701d864d227d5071da3e5149609ba465 to e4a41f124952825288dd2dc170cf89025f549da6 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:54:45 to 01/21/2026 22:55:53 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 881b91a9701d864d227d5071da3e5149609ba465 to e4a41f124952825288dd2dc170cf89025f549da6 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:54:45 to 01/21/2026 22:55:53 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 8aa6ea4e1 - 2026-01-21 16:55:56 -0600 - 01/21/2026 16:55:56
Added in Other:
- DFFlagEnableSystrayExpEnrollment_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:53:30 | Mechanism: Enables a system tray for user experience enrollment. | Purpose: Allows players to easily opt into new features and experiences.
- FFlagAmrFixCustomizeGroups_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;1964796395;2026-01-21T22:51:36 | Mechanism: Fixes issues with customizing group settings in the avatar system. | Purpose: Allows players to better customize their groups without errors.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 25233a4d05b858a73c203143821ddd75c51ba49d to 881b91a9701d864d227d5071da3e5149609ba465 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:52:29 to 01/21/2026 22:54:45 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 25233a4d05b858a73c203143821ddd75c51ba49d to 881b91a9701d864d227d5071da3e5149609ba465 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:52:29 to 01/21/2026 22:54:45 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## f1b41ee87 - 2026-01-21 16:53:39 -0600 - 01/21/2026 16:53:39
Added in Other:
- DFFlagEnableSystrayBackgroundAppUpdate_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:50:10 | Mechanism: Allows the app to update in the background via the system tray. | Purpose: Keeps the app up to date without interrupting the player's experience.
- DFFlagRbxStorageAvailableSpaceCreatePath = True | Mechanism: Creates a path for checking available storage space in Roblox. | Purpose: Helps players manage their storage more effectively, ensuring they have enough space for new content.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 07ebce712294862765b5e250fdf80a9d350897cc to 25233a4d05b858a73c203143821ddd75c51ba49d | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:50:31 to 01/21/2026 22:52:29 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 07ebce712294862765b5e250fdf80a9d350897cc to 25233a4d05b858a73c203143821ddd75c51ba49d | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:50:31 to 01/21/2026 22:52:29 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- DFFlagRbxStorageAvailableSpaceCreatePath_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:46:36) | Mechanism: Enables a new method for checking available storage space when creating paths in Roblox. | Purpose: Helps developers avoid errors related to storage limits, ensuring smoother game development.

## d04739481 - 2026-01-21 16:51:21 -0600 - 01/21/2026 16:51:21
Added in Other:
- FFlagSystemTrayDeviceSettings2_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:47:38 | Mechanism: Implements new device settings accessible from the system tray. | Purpose: Provides players with easier access to device settings for a better gaming experience.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 1853aa14cf2ee474bcbb235e8fe40c7c4913e4fb to 07ebce712294862765b5e250fdf80a9d350897cc | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:47:41 to 01/21/2026 22:50:31 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 1853aa14cf2ee474bcbb235e8fe40c7c4913e4fb to 07ebce712294862765b5e250fdf80a9d350897cc | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:47:41 to 01/21/2026 22:50:31 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 8146a11cf - 2026-01-21 16:49:05 -0600 - 01/21/2026 16:49:04
Added in Other:
- DFFlagRemoveTrayUserAgentKeyword_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:45:24 | Mechanism: Removes specific keywords from the user agent string sent to servers. | Purpose: Enhances privacy and security for players by not revealing unnecessary information.
- DFIntSystrayEventsThrottleHundredthsPercent_Staged = 10000;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:46:36 | Mechanism: Adjusts the frequency of system tray event notifications. | Purpose: Reduces notification clutter, allowing players to focus on their games without distractions.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from cdb17f1c8ae9f948d0e2c31272cab4f083b5698c to 1853aa14cf2ee474bcbb235e8fe40c7c4913e4fb | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:37:05 to 01/21/2026 22:47:41 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from cdb17f1c8ae9f948d0e2c31272cab4f083b5698c to 1853aa14cf2ee474bcbb235e8fe40c7c4913e4fb | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:37:05 to 01/21/2026 22:47:41 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 815145c81 - 2026-01-21 16:37:50 -0600 - 01/21/2026 16:37:50
Added in Other:
- DFFlagDirectMipCalc = True | Mechanism: Calculates texture details more directly for better performance. | Purpose: Enhances visual quality and performance of graphics in games for players.
Added in Graphics:
- FFlagFixFalseMipTextureFree = True | Mechanism: Corrects issues with texture quality in games. | Purpose: Improves the visual quality of games, making them look better for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 2845f51cd3ab4a6c077f166da8c282dc974799ad to cdb17f1c8ae9f948d0e2c31272cab4f083b5698c | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:31:49 to 01/21/2026 22:37:05 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 2845f51cd3ab4a6c077f166da8c282dc974799ad to cdb17f1c8ae9f948d0e2c31272cab4f083b5698c | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:31:49 to 01/21/2026 22:37:05 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- DFFlagDirectMipCalc_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:32:06) | Mechanism: Calculates mipmaps directly for better texture rendering. | Purpose: Enhances texture quality and performance in games.
Removed in Graphics:
- FFlagFixFalseMipTextureFree_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:31:28) | Mechanism: Addresses problems with texture loading that incorrectly displays lower-quality images. | Purpose: Improves visual quality by ensuring textures load correctly, enhancing the overall game experience.

## 0a200fb48 - 2026-01-21 16:33:21 -0600 - 01/21/2026 16:33:20
Added in Graphics:
- FFlagSharedResolutionTexture = True | Mechanism: Allows textures to share resolution settings across different assets. | Purpose: Reduces loading times and improves visual consistency in games.
Added in Network:
- SFFlagIAS_InstancePointersHoldAcrossReplication3 = True | Mechanism: Allows instance pointers to remain valid even when replicated across different game servers. | Purpose: Improves the consistency of object references for developers, making it easier to manage game elements.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 9e37925a479ece59fc438bde3f6bc0a3f24a1234 to 2845f51cd3ab4a6c077f166da8c282dc974799ad | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:27:24 to 01/21/2026 22:31:49 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 9e37925a479ece59fc438bde3f6bc0a3f24a1234 to 2845f51cd3ab4a6c077f166da8c282dc974799ad | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:27:24 to 01/21/2026 22:31:49 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Graphics:
- FFlagSharedResolutionTexture_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:29:15) | Mechanism: Allows textures to share resolution settings across different assets. | Purpose: Reduces loading times and improves visual consistency in games.
Removed in Network:
- SFFlagIAS_InstancePointersHoldAcrossReplication3_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:28:00) | Mechanism: Allows instance pointers to remain consistent during data replication. | Purpose: Enhances the stability and reliability of game data across different players' experiences.

## eb9bae87c - 2026-01-21 16:28:51 -0600 - 01/21/2026 16:28:51
Added in Other:
- FFlagLuaAppGameTileWideVideoThumbnail_Staged = false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:25:00 | Mechanism: Enables wider video thumbnails for game tiles in the app. | Purpose: Enhances visual appeal and engagement by showcasing game videos more prominently.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 582a5d0cf4413e398c608d9e9bb97fa77c618606 to 9e37925a479ece59fc438bde3f6bc0a3f24a1234 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:25:07 to 01/21/2026 22:27:24 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 582a5d0cf4413e398c608d9e9bb97fa77c618606 to 9e37925a479ece59fc438bde3f6bc0a3f24a1234 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:25:07 to 01/21/2026 22:27:24 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- DFFlagRM3ScreenshotEncoding_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:22:26) | Mechanism: Implements a new method for encoding screenshots taken in the game. | Purpose: Improves the quality and efficiency of screenshots for players.

## b524dedc0 - 2026-01-21 16:26:34 -0600 - 01/21/2026 16:26:34
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 449630fa629f532568e01e248ba75ebbbc36abaf to 582a5d0cf4413e398c608d9e9bb97fa77c618606 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:22:17 to 01/21/2026 22:25:07 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 449630fa629f532568e01e248ba75ebbbc36abaf to 582a5d0cf4413e398c608d9e9bb97fa77c618606 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:22:17 to 01/21/2026 22:25:07 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 91a647c24 - 2026-01-21 16:24:17 -0600 - 01/21/2026 16:24:17
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from c6b23707e0f83b26f6577dd4111e50500f9fa74b to 449630fa629f532568e01e248ba75ebbbc36abaf | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:19:16 to 01/21/2026 22:22:17 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from c6b23707e0f83b26f6577dd4111e50500f9fa74b to 449630fa629f532568e01e248ba75ebbbc36abaf | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:19:16 to 01/21/2026 22:22:17 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## fa24ca6a0 - 2026-01-21 16:22:00 -0600 - 01/21/2026 16:22:00
Added in Other:
- DFFlagUseCompletedRadiusFunc_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:18:16 | Mechanism: Uses a new function for calculating radius in game physics. | Purpose: Enhances the accuracy of physics interactions in the game.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 0b9b25059d7a319b6b1b7dc82608308192524dec to c6b23707e0f83b26f6577dd4111e50500f9fa74b | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:18:02 to 01/21/2026 22:19:16 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 0b9b25059d7a319b6b1b7dc82608308192524dec to c6b23707e0f83b26f6577dd4111e50500f9fa74b | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:18:02 to 01/21/2026 22:19:16 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## b80e388c4 - 2026-01-21 16:19:44 -0600 - 01/21/2026 16:19:44
Added in Other:
- DFFlagMoveEverythingA = True | Mechanism: Changes the way certain game elements are organized or processed. | Purpose: Streamlines game performance and improves the overall player experience.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 9e3e08638d4b22a85857a00fa7a0a11f865055f5 to 0b9b25059d7a319b6b1b7dc82608308192524dec | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:16:27 to 01/21/2026 22:18:02 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 9e3e08638d4b22a85857a00fa7a0a11f865055f5 to 0b9b25059d7a319b6b1b7dc82608308192524dec | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:16:27 to 01/21/2026 22:18:02 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- DFFlagMoveEverythingA_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:13:03) | Mechanism: Allows players to move UI elements freely on the screen. | Purpose: Gives players more control over their interface layout for a personalized experience.

## ec94a7a7a - 2026-01-21 16:17:26 -0600 - 01/21/2026 16:17:25
Added in Other:
- DFFlagCLI184446_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:12:37 | Mechanism: Implements a staged rollout of a command-line interface feature. | Purpose: Allows developers to test new features safely before full release.
Added in Camera/UI:
- FFlagAbuseReportMenuScreenshotReduceMotionFix_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:13:20 | Mechanism: Reduces motion effects in the abuse report menu when taking screenshots. | Purpose: Makes it easier for players to capture and report issues without distractions.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 3da39ebf8e753906b7e53a482c1f160ce04a315c to 9e3e08638d4b22a85857a00fa7a0a11f865055f5 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:13:33 to 01/21/2026 22:16:27 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 3da39ebf8e753906b7e53a482c1f160ce04a315c to 9e3e08638d4b22a85857a00fa7a0a11f865055f5 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:13:33 to 01/21/2026 22:16:27 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 9703d8646 - 2026-01-21 16:15:08 -0600 - 01/21/2026 16:15:08
Added in Other:
- FFlagAXScrollingListAutomaticCanvasSize_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:11:33 | Mechanism: Automatically adjusts the size of scrolling lists based on content. | Purpose: Ensures that lists display correctly without unnecessary scrolling, enhancing usability.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 31f7091498c64d6a44eff7702f5f55e3f769eaf2 to 3da39ebf8e753906b7e53a482c1f160ce04a315c | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:07:36 to 01/21/2026 22:13:33 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 31f7091498c64d6a44eff7702f5f55e3f769eaf2 to 3da39ebf8e753906b7e53a482c1f160ce04a315c | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:07:36 to 01/21/2026 22:13:33 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 9959061a8 - 2026-01-21 16:08:26 -0600 - 01/21/2026 16:08:25
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 5e60fea1180cdea2dac00d067cafc332d054e396 to 31f7091498c64d6a44eff7702f5f55e3f769eaf2 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:02:31 to 01/21/2026 22:07:36 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 5e60fea1180cdea2dac00d067cafc332d054e396 to 31f7091498c64d6a44eff7702f5f55e3f769eaf2 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:02:31 to 01/21/2026 22:07:36 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## ef0c006cf - 2026-01-21 16:03:48 -0600 - 01/21/2026 16:03:47
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 1a45740107331f6e9aa14115277abc2e8e72d6cb to 5e60fea1180cdea2dac00d067cafc332d054e396 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:57:20 to 01/21/2026 22:02:31 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 1a45740107331f6e9aa14115277abc2e8e72d6cb to 5e60fea1180cdea2dac00d067cafc332d054e396 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:57:20 to 01/21/2026 22:02:31 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## a12151612 - 2026-01-21 15:59:15 -0600 - 01/21/2026 15:59:15
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from bb9ab32df6425cc4c3f7e85fe66b88fde559ad15 to 1a45740107331f6e9aa14115277abc2e8e72d6cb | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:50:11 to 01/21/2026 21:57:20 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from bb9ab32df6425cc4c3f7e85fe66b88fde559ad15 to 1a45740107331f6e9aa14115277abc2e8e72d6cb | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:50:11 to 01/21/2026 21:57:20 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## c23a1b2ba - 2026-01-21 15:52:32 -0600 - 01/21/2026 15:52:32
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from cc133b37285c49892eb75a0361ab1e1387102f4a to bb9ab32df6425cc4c3f7e85fe66b88fde559ad15 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:49:20 to 01/21/2026 21:50:11 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from cc133b37285c49892eb75a0361ab1e1387102f4a to bb9ab32df6425cc4c3f7e85fe66b88fde559ad15 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:49:20 to 01/21/2026 21:50:11 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## f8ca62eba - 2026-01-21 15:50:14 -0600 - 01/21/2026 15:50:14
Added in Other:
- DFFlagRbxStorageAvailableSpaceCreatePath_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:46:36 | Mechanism: Enables a new method for checking available storage space when creating paths in Roblox. | Purpose: Helps developers avoid errors related to storage limits, ensuring smoother game development.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 90752e8aeee65744c5ad35eaed23a626c365b1ca to cc133b37285c49892eb75a0361ab1e1387102f4a | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:45:13 to 01/21/2026 21:49:20 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 90752e8aeee65744c5ad35eaed23a626c365b1ca to cc133b37285c49892eb75a0361ab1e1387102f4a | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:45:13 to 01/21/2026 21:49:20 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 4914296be - 2026-01-21 15:45:41 -0600 - 01/21/2026 15:45:41
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from aac2d6115b8e3b703c4acc59e73edaffb6908c6d to 90752e8aeee65744c5ad35eaed23a626c365b1ca | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:42:27 to 01/21/2026 21:45:13 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from aac2d6115b8e3b703c4acc59e73edaffb6908c6d to 90752e8aeee65744c5ad35eaed23a626c365b1ca | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:42:27 to 01/21/2026 21:45:13 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## dfd809adf - 2026-01-21 15:43:23 -0600 - 01/21/2026 15:43:22
Added in Camera/UI:
- FFlagUIBloxFixCoplayFooterConditionalHooks = True | Mechanism: Fixes issues with conditional hooks in the CoPlay footer of the UI. | Purpose: Ensures a smoother and more reliable user interface for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 32762cbefbe153de084846b4ac90d60b0deefbac to aac2d6115b8e3b703c4acc59e73edaffb6908c6d | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:36:38 to 01/21/2026 21:42:27 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 32762cbefbe153de084846b4ac90d60b0deefbac to aac2d6115b8e3b703c4acc59e73edaffb6908c6d | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:36:38 to 01/21/2026 21:42:27 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Camera/UI:
- FFlagUIBloxFixCoplayFooterConditionalHooks_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T20:36:56) | Mechanism: Fixes issues with conditional rendering in the UI framework for co-play features. | Purpose: Enhances the user interface for players during co-play sessions, making it more reliable.

## 53b45efa5 - 2026-01-21 15:38:51 -0600 - 01/21/2026 15:38:50
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from abc0e8bcacbebc582e3219186e22a4cc14734b45 to 32762cbefbe153de084846b4ac90d60b0deefbac | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:35:55 to 01/21/2026 21:36:38 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from abc0e8bcacbebc582e3219186e22a4cc14734b45 to 32762cbefbe153de084846b4ac90d60b0deefbac | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:35:55 to 01/21/2026 21:36:38 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagAXScrollingListAutomaticCanvasSize_Staged removed (was true;SteadyState;10;30;Revert;2026-01-21T21:02:56) | Mechanism: Automatically adjusts the size of scrolling lists based on content. | Purpose: Ensures that lists display correctly without unnecessary scrolling, enhancing usability.

## 4a52d9364 - 2026-01-21 15:36:31 -0600 - 01/21/2026 15:36:31
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from c2a023751525f464983db21f0f9adada51d83975 to abc0e8bcacbebc582e3219186e22a4cc14734b45 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:32:57 to 01/21/2026 21:35:55 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from c2a023751525f464983db21f0f9adada51d83975 to abc0e8bcacbebc582e3219186e22a4cc14734b45 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:32:57 to 01/21/2026 21:35:55 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 1996c6303 - 2026-01-21 15:34:14 -0600 - 01/21/2026 15:34:13
Added in Other:
- DFFlagDirectMipCalc_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:32:06 | Mechanism: Calculates mipmaps directly for better texture rendering. | Purpose: Enhances texture quality and performance in games.
Added in Graphics:
- FFlagFixFalseMipTextureFree_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:31:28 | Mechanism: Addresses problems with texture loading that incorrectly displays lower-quality images. | Purpose: Improves visual quality by ensuring textures load correctly, enhancing the overall game experience.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 3c05c547f3cb1d5aa2e83347a9ec611ba98e0df6 to c2a023751525f464983db21f0f9adada51d83975 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:29:56 to 01/21/2026 21:32:57 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 3c05c547f3cb1d5aa2e83347a9ec611ba98e0df6 to c2a023751525f464983db21f0f9adada51d83975 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:29:56 to 01/21/2026 21:32:57 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 6f2ddc0b8 - 2026-01-21 15:31:55 -0600 - 01/21/2026 15:31:54
Added in Graphics:
- FFlagSharedResolutionTexture_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:29:15 | Mechanism: Allows textures to share resolution settings across different assets. | Purpose: Reduces loading times and improves visual consistency in games.
Added in Network:
- SFFlagIAS_InstancePointersHoldAcrossReplication3_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:28:00 | Mechanism: Allows instance pointers to remain consistent during data replication. | Purpose: Enhances the stability and reliability of game data across different players' experiences.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 38324140fd14a0ae04281d66f9b19bcff5f5a9cd to 3c05c547f3cb1d5aa2e83347a9ec611ba98e0df6 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:23:17 to 01/21/2026 21:29:56 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 38324140fd14a0ae04281d66f9b19bcff5f5a9cd to 3c05c547f3cb1d5aa2e83347a9ec611ba98e0df6 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:23:17 to 01/21/2026 21:29:56 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## f9362faaf - 2026-01-21 15:25:00 -0600 - 01/21/2026 15:25:00
Added in Other:
- DFFlagRM3ScreenshotEncoding_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:22:26 | Mechanism: Implements a new method for encoding screenshots taken in the game. | Purpose: Improves the quality and efficiency of screenshots for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from d731728a8e85b42d336d4240430ae07b72c9cd88 to 38324140fd14a0ae04281d66f9b19bcff5f5a9cd | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:21:29 to 01/21/2026 21:23:17 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from d731728a8e85b42d336d4240430ae07b72c9cd88 to 38324140fd14a0ae04281d66f9b19bcff5f5a9cd | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:21:29 to 01/21/2026 21:23:17 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## d2e676a88 - 2026-01-21 15:22:40 -0600 - 01/21/2026 15:22:40
Added in Other:
- FFlagLogRewardedVideoPlayerButtonActions = True | Mechanism: Tracks user interactions with rewarded video player buttons. | Purpose: Helps developers understand player engagement with ads for better rewards.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from b6e7b33fc3aeda92256ce2095ceab2774b53757a to d731728a8e85b42d336d4240430ae07b72c9cd88 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:16:59 to 01/21/2026 21:21:29 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from b6e7b33fc3aeda92256ce2095ceab2774b53757a to d731728a8e85b42d336d4240430ae07b72c9cd88 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:16:59 to 01/21/2026 21:21:29 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- DFFlagRM3ScreenshotEncoding_Staged removed (was false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:07:09) | Mechanism: Implements a new method for encoding screenshots taken in the game. | Purpose: Improves the quality and efficiency of screenshots for players.
- FFlagLogRewardedVideoPlayerButtonActions_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T20:17:30) | Mechanism: Records user interactions with buttons in the rewarded video player. | Purpose: Helps developers understand player behavior and improve video ad experiences.
Removed in Network:
- SFFlagIAS_InstancePointersHoldAcrossReplication3_Staged removed (was true;SteadyState;10;30;Revert;2026-01-21T20:45:51) | Mechanism: Allows instance pointers to remain consistent during data replication. | Purpose: Enhances the stability and reliability of game data across different players' experiences.

## eda0beb5c - 2026-01-21 15:18:08 -0600 - 01/21/2026 15:18:07
Added in Other:
- FFlagExplorerOptimizedHasChildren = True | Mechanism: Improves the performance of the Explorer panel by optimizing how it handles child objects. | Purpose: Makes it faster and smoother for developers to navigate and manage their game objects.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from e41df4de257ae477f4e8b4e76ec7ff0505978f97 to b6e7b33fc3aeda92256ce2095ceab2774b53757a | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:14:57 to 01/21/2026 21:16:59 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from e41df4de257ae477f4e8b4e76ec7ff0505978f97 to b6e7b33fc3aeda92256ce2095ceab2774b53757a | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:14:57 to 01/21/2026 21:16:59 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagExplorerOptimizedHasChildren_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T20:12:57) | Mechanism: Optimizes how the Explorer panel checks for child objects in the game hierarchy. | Purpose: Improves performance for developers using the Explorer, making it easier to manage game objects.

## 3dd316d65 - 2026-01-21 15:15:49 -0600 - 01/21/2026 15:15:49
Added in Other:
- DFFlagMoveEverythingA_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:13:03 | Mechanism: Allows players to move UI elements freely on the screen. | Purpose: Gives players more control over their interface layout for a personalized experience.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 901307ffcc0e08f8e4e80075dbba6e3d46ea28e4 to e41df4de257ae477f4e8b4e76ec7ff0505978f97 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:12:39 to 01/21/2026 21:14:57 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 901307ffcc0e08f8e4e80075dbba6e3d46ea28e4 to e41df4de257ae477f4e8b4e76ec7ff0505978f97 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:12:39 to 01/21/2026 21:14:57 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## ce8a6abaf - 2026-01-21 15:13:32 -0600 - 01/21/2026 15:13:31
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from f8007fbaa09958c98f744102a25400f72142cbd7 to 901307ffcc0e08f8e4e80075dbba6e3d46ea28e4 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:07:50 to 01/21/2026 21:12:39 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from f8007fbaa09958c98f744102a25400f72142cbd7 to 901307ffcc0e08f8e4e80075dbba6e3d46ea28e4 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:07:50 to 01/21/2026 21:12:39 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## c0098da68 - 2026-01-21 15:08:57 -0600 - 01/21/2026 15:08:56
Added in Other:
- DFFlagRM3ScreenshotEncoding_Staged = false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:07:09 | Mechanism: Implements a new method for encoding screenshots taken in the game. | Purpose: Improves the quality and efficiency of screenshots for players.
- FFlagVideoEnableHevcEncode2 = True | Mechanism: Enables HEVC encoding for video uploads, improving compression efficiency. | Purpose: Allows players to upload higher quality videos with smaller file sizes.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from bdf99dafac5c5c782ae10d14fb13df05a9247d75 to f8007fbaa09958c98f744102a25400f72142cbd7 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:03:51 to 01/21/2026 21:07:50 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from bdf99dafac5c5c782ae10d14fb13df05a9247d75 to f8007fbaa09958c98f744102a25400f72142cbd7 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:03:51 to 01/21/2026 21:07:50 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagVideoEnableHevcEncode2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T20:04:39) | Mechanism: Enables HEVC video encoding for better compression. | Purpose: Provides higher quality video streaming with less data usage for players.

## d6c2bb923 - 2026-01-21 15:06:39 -0600 - 01/21/2026 15:06:38
Added in Other:
- FFlagAXScrollingListAutomaticCanvasSize_Staged = true;SteadyState;10;30;Revert;2026-01-21T21:02:56 | Mechanism: Automatically adjusts the size of scrolling lists based on content. | Purpose: Ensures that lists display correctly without unnecessary scrolling, enhancing usability.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 0b7b92c3fd2c4bfc3561143b4cfdd20b30a27078 to bdf99dafac5c5c782ae10d14fb13df05a9247d75 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:01:54 to 01/21/2026 21:03:51 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 0b7b92c3fd2c4bfc3561143b4cfdd20b30a27078 to bdf99dafac5c5c782ae10d14fb13df05a9247d75 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:01:54 to 01/21/2026 21:03:51 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## f12c8e212 - 2026-01-21 15:04:21 -0600 - 01/21/2026 15:04:21
Added in Camera/UI:
- FFlagAXCatalogCategoriesSDUILinks = True | Mechanism: Introduces links in the catalog categories that are designed for a better user interface. | Purpose: Enhances the browsing experience for players, making it easier to find and access items.
- FFlagAXCatalogCategoriesSDUITaxonomy = True | Mechanism: Updates the catalog categories to a new taxonomy structure. | Purpose: Enhances the organization of items in the catalog, making it easier for players to find what they want.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 450679fcf049b6fc257d41094f5cb950240b682f to 0b7b92c3fd2c4bfc3561143b4cfdd20b30a27078 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:00:43 to 01/21/2026 21:01:54 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 450679fcf049b6fc257d41094f5cb950240b682f to 0b7b92c3fd2c4bfc3561143b4cfdd20b30a27078 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:00:43 to 01/21/2026 21:01:54 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Camera/UI:
- FFlagAXCatalogCategoriesSDUILinks_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T19:59:04) | Mechanism: Implements new links in the catalog categories for easier navigation. | Purpose: Makes it simpler for players to find and access different items in the catalog.
- FFlagAXCatalogCategoriesSDUITaxonomy_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T20:00:27) | Mechanism: Updates the categorization system in the catalog to better organize items. | Purpose: Makes it easier for players to find and browse items in the catalog, improving shopping experience.

## 8bd9cf64f - 2026-01-21 15:02:04 -0600 - 01/21/2026 15:02:04
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from fa0d3fb55299a6c58c2fae58bdc036bbb5fac017 to 450679fcf049b6fc257d41094f5cb950240b682f | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:53:11 to 01/21/2026 21:00:43 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from fa0d3fb55299a6c58c2fae58bdc036bbb5fac017 to 450679fcf049b6fc257d41094f5cb950240b682f | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:53:11 to 01/21/2026 21:00:43 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 9ad39011e - 2026-01-21 14:55:20 -0600 - 01/21/2026 14:55:20
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from b2e885bc1e7886299ea3f8fdc811f871cfc53a54 to fa0d3fb55299a6c58c2fae58bdc036bbb5fac017 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:51:23 to 01/21/2026 20:53:11 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from b2e885bc1e7886299ea3f8fdc811f871cfc53a54 to fa0d3fb55299a6c58c2fae58bdc036bbb5fac017 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:51:23 to 01/21/2026 20:53:11 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## c49dedb52 - 2026-01-21 14:53:00 -0600 - 01/21/2026 14:52:59
Added in Other:
- FFlagDevConsoleDownArrowIconFix = True | Mechanism: Fixes the icon for the down arrow in the developer console. | Purpose: Enhances usability for developers, making it easier to navigate the console.
- FFlagExplorerHeartbeatTelemetry = True | Mechanism: Collects data on the performance and usage of the Explorer tool in Roblox Studio. | Purpose: Helps improve the Explorer tool by understanding how players use it.
Added in Network:
- SFFlagIAS_InstancePointersHoldAcrossReplication3_Staged = true;SteadyState;10;30;Revert;2026-01-21T20:45:51 | Mechanism: Allows instance pointers to remain consistent during data replication. | Purpose: Enhances the stability and reliability of game data across different players' experiences.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from daa1d23702142d404000396bcf617f09b79dd2d4 to b2e885bc1e7886299ea3f8fdc811f871cfc53a54 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:46:51 to 01/21/2026 20:51:23 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from daa1d23702142d404000396bcf617f09b79dd2d4 to b2e885bc1e7886299ea3f8fdc811f871cfc53a54 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:46:51 to 01/21/2026 20:51:23 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagDevConsoleDownArrowIconFix_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T19:48:10) | Mechanism: Fixes the icon display for the down arrow in the developer console. | Purpose: Improves the visual clarity of the developer console for better usability.
- FFlagExplorerHeartbeatTelemetry_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T19:49:24) | Mechanism: Collects data on the performance of the Explorer tool in real-time. | Purpose: Helps improve the Explorer tool's performance and reliability for developers.

## f8de25296 - 2026-01-21 14:48:27 -0600 - 01/21/2026 14:48:27
Added in Other:
- FFlagGImageWebPBiEndianLoad = True | Mechanism: Enables loading of WebP images in a bi-endian format. | Purpose: Improves image loading efficiency and quality for better visuals.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from cc08b0748478379ff55c5ebe6b1ed649b55f1deb to daa1d23702142d404000396bcf617f09b79dd2d4 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:39:23 to 01/21/2026 20:46:51 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from cc08b0748478379ff55c5ebe6b1ed649b55f1deb to daa1d23702142d404000396bcf617f09b79dd2d4 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:39:23 to 01/21/2026 20:46:51 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagGImageWebPBiEndianLoad_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T19:44:39) | Mechanism: Enables loading WebP images in a specific byte order. | Purpose: Improves image loading performance for certain graphics.
- FFlagRbxTelemetryEnableHttpRetries3_Staged removed (was true;SteadyState;10;30;Revert;true;387806565;2026-01-21T20:12:35) | Mechanism: Enables retry logic for HTTP requests to ensure data is sent and received reliably. | Purpose: Improves the stability of in-game features that rely on internet connectivity, enhancing overall gameplay experience.
- FFlagTelemetryRetryOnConnectFail_Staged removed (was true;SteadyState;10;30;Revert;true;387806565;2026-01-21T20:12:35) | Mechanism: Retries connection attempts when the initial connection fails. | Purpose: Increases reliability of connections, reducing disruptions for players.
- FFlagTelemetryRetryOnDnsResolve_Staged removed (was true;SteadyState;10;30;Revert;true;387806565;2026-01-21T20:12:35) | Mechanism: Retries DNS resolution if it fails initially. | Purpose: Ensures more stable connections by reducing the chance of failed lookups.

## 9910228b4 - 2026-01-21 14:41:42 -0600 - 01/21/2026 14:41:42
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 9ef98c7f3eaf3b6d77c3aee402fa2d8ee26d84b6 to cc08b0748478379ff55c5ebe6b1ed649b55f1deb | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:37:36 to 01/21/2026 20:39:23 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 9ef98c7f3eaf3b6d77c3aee402fa2d8ee26d84b6 to cc08b0748478379ff55c5ebe6b1ed649b55f1deb | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:37:36 to 01/21/2026 20:39:23 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 34296b928 - 2026-01-21 14:39:24 -0600 - 01/21/2026 14:39:24
Added in Camera/UI:
- FFlagUIBloxFixCoplayFooterConditionalHooks_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T20:36:56 | Mechanism: Fixes issues with conditional rendering in the UI framework for co-play features. | Purpose: Enhances the user interface for players during co-play sessions, making it more reliable.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from a14617adee757464cf654de1043f08281ecf00df to 9ef98c7f3eaf3b6d77c3aee402fa2d8ee26d84b6 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:26:39 to 01/21/2026 20:37:36 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from a14617adee757464cf654de1043f08281ecf00df to 9ef98c7f3eaf3b6d77c3aee402fa2d8ee26d84b6 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:26:39 to 01/21/2026 20:37:36 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 0a4398250 - 2026-01-21 14:28:08 -0600 - 01/21/2026 14:28:08
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from e6b92db3c0a09b4e01e5178d18a8dfe5457b63d8 to a14617adee757464cf654de1043f08281ecf00df | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:21:59 to 01/21/2026 20:26:39 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from e6b92db3c0a09b4e01e5178d18a8dfe5457b63d8 to a14617adee757464cf654de1043f08281ecf00df | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:21:59 to 01/21/2026 20:26:39 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 32c2925d6 - 2026-01-21 14:23:36 -0600 - 01/21/2026 14:23:35
Added in Other:
- FFlagAXHandleCategoryIdsTaxonomyDeepLinks = True | Mechanism: Enables deep linking to specific categories within the game. | Purpose: Helps players quickly access specific game categories or items directly.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from a9c35f35c602fd078e2d140fecc0275ff319afb7 to e6b92db3c0a09b4e01e5178d18a8dfe5457b63d8 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:18:37 to 01/21/2026 20:21:59 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from a9c35f35c602fd078e2d140fecc0275ff319afb7 to e6b92db3c0a09b4e01e5178d18a8dfe5457b63d8 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:18:37 to 01/21/2026 20:21:59 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagAXHandleCategoryIdsTaxonomyDeepLinks_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T19:19:47) | Mechanism: Improves how category links are managed for game content. | Purpose: Enhances navigation for players by making it easier to find specific game categories.

## 3bdca36ca - 2026-01-21 14:21:17 -0600 - 01/21/2026 14:21:17
Added in Other:
- FFlagLogRewardedVideoPlayerButtonActions_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T20:17:30 | Mechanism: Records user interactions with buttons in the rewarded video player. | Purpose: Helps developers understand player behavior and improve video ad experiences.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 09b0408f0a8c343b469d7572b7ceb9c3c1b15e49 to a9c35f35c602fd078e2d140fecc0275ff319afb7 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:16:39 to 01/21/2026 20:18:37 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 09b0408f0a8c343b469d7572b7ceb9c3c1b15e49 to a9c35f35c602fd078e2d140fecc0275ff319afb7 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:16:39 to 01/21/2026 20:18:37 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 3250c9c80 - 2026-01-21 14:19:02 -0600 - 01/21/2026 14:19:01
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 12d90f13dd212f30bd479e4722f2201703d99f34 to 09b0408f0a8c343b469d7572b7ceb9c3c1b15e49 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:15:44 to 01/21/2026 20:16:39 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 12d90f13dd212f30bd479e4722f2201703d99f34 to 09b0408f0a8c343b469d7572b7ceb9c3c1b15e49 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:15:44 to 01/21/2026 20:16:39 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## de393de46 - 2026-01-21 14:16:45 -0600 - 01/21/2026 14:16:45
Added in Other:
- FFlagExplorerOptimizedHasChildren_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T20:12:57 | Mechanism: Optimizes how the Explorer panel checks for child objects in the game hierarchy. | Purpose: Improves performance for developers using the Explorer, making it easier to manage game objects.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 25fb87dd6a515dcb2e6c789fbf00672ea29b8e13 to 12d90f13dd212f30bd479e4722f2201703d99f34 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:13:45 to 01/21/2026 20:15:44 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 25fb87dd6a515dcb2e6c789fbf00672ea29b8e13 to 12d90f13dd212f30bd479e4722f2201703d99f34 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:13:45 to 01/21/2026 20:15:44 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 1ab70b8fc - 2026-01-21 14:14:28 -0600 - 01/21/2026 14:14:27
Added in Other:
- FFlagRbxTelemetryEnableHttpRetries3_Staged = true;SteadyState;10;30;Revert;true;387806565;2026-01-21T20:12:35 | Mechanism: Enables retry logic for HTTP requests to ensure data is sent and received reliably. | Purpose: Improves the stability of in-game features that rely on internet connectivity, enhancing overall gameplay experience.
- FFlagTelemetryRetryOnConnectFail_Staged = true;SteadyState;10;30;Revert;true;387806565;2026-01-21T20:12:35 | Mechanism: Retries connection attempts when the initial connection fails. | Purpose: Increases reliability of connections, reducing disruptions for players.
- FFlagTelemetryRetryOnDnsResolve_Staged = true;SteadyState;10;30;Revert;true;387806565;2026-01-21T20:12:35 | Mechanism: Retries DNS resolution if it fails initially. | Purpose: Ensures more stable connections by reducing the chance of failed lookups.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from f4e456e90dc749ecbb1a6b4fe08e51c335f212b2 to 25fb87dd6a515dcb2e6c789fbf00672ea29b8e13 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:07:03 to 01/21/2026 20:13:45 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from f4e456e90dc749ecbb1a6b4fe08e51c335f212b2 to 25fb87dd6a515dcb2e6c789fbf00672ea29b8e13 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:07:03 to 01/21/2026 20:13:45 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## a48dc5ce8 - 2026-01-21 14:09:58 -0600 - 01/21/2026 14:09:57
Added in Other:
- FFlagPerformanceControlBudgetSystemRollout10 = True | Mechanism: Implements a system to manage performance budgets for games. | Purpose: Ensures games run efficiently, providing a smoother experience for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from c1ebc76569cdd3ca06fb074a154ba0ff78783b0c to f4e456e90dc749ecbb1a6b4fe08e51c335f212b2 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:05:39 to 01/21/2026 20:07:03 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from c1ebc76569cdd3ca06fb074a154ba0ff78783b0c to f4e456e90dc749ecbb1a6b4fe08e51c335f212b2 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:05:39 to 01/21/2026 20:07:03 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagPerformanceControlBudgetSystemRollout10_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:58:31) | Mechanism: Introduces a new system to manage performance budgets. | Purpose: Optimizes game performance, leading to smoother gameplay for players.

## 560b9e725 - 2026-01-21 14:07:43 -0600 - 01/21/2026 14:07:43
Added in Other:
- FFlagVideoEnableHevcEncode2_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T20:04:39 | Mechanism: Enables HEVC video encoding for better compression. | Purpose: Provides higher quality video streaming with less data usage for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from bbb1aec0bacfa2729cfcf8a2e434ec297afff547 to c1ebc76569cdd3ca06fb074a154ba0ff78783b0c | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:01:12 to 01/21/2026 20:05:39 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from bbb1aec0bacfa2729cfcf8a2e434ec297afff547 to c1ebc76569cdd3ca06fb074a154ba0ff78783b0c | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:01:12 to 01/21/2026 20:05:39 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 1e4165c94 - 2026-01-21 14:03:12 -0600 - 01/21/2026 14:03:11
Added in Camera/UI:
- FFlagAXCatalogCategoriesSDUITaxonomy_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T20:00:27 | Mechanism: Updates the categorization system in the catalog to better organize items. | Purpose: Makes it easier for players to find and browse items in the catalog, improving shopping experience.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 6d958c3d9bedd893cbfc975f6b702ce946a9e004 to bbb1aec0bacfa2729cfcf8a2e434ec297afff547 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 19:59:58 to 01/21/2026 20:01:12 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 6d958c3d9bedd893cbfc975f6b702ce946a9e004 to bbb1aec0bacfa2729cfcf8a2e434ec297afff547 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 19:59:58 to 01/21/2026 20:01:12 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## af34c3280 - 2026-01-21 14:00:54 -0600 - 01/21/2026 14:00:53
Added in Camera/UI:
- FFlagAXCatalogCategoriesSDUILinks_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T19:59:04 | Mechanism: Implements new links in the catalog categories for easier navigation. | Purpose: Makes it simpler for players to find and access different items in the catalog.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from ab78fe8e4d722b6661bd4229ae1d08c2417ef544 to 6d958c3d9bedd893cbfc975f6b702ce946a9e004 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 19:57:04 to 01/21/2026 19:59:58 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from ab78fe8e4d722b6661bd4229ae1d08c2417ef544 to 6d958c3d9bedd893cbfc975f6b702ce946a9e004 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 19:57:04 to 01/21/2026 19:59:58 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## c5d94883f - 2026-01-21 13:58:37 -0600 - 01/21/2026 13:58:36
Added in Other:
- FFlagAndroidHevcEncoderCheck = True | Mechanism: Enables checking for HEVC encoder support on Android devices. | Purpose: Allows better video quality during gameplay on supported devices.
- FFlagEnablePackagePublishFailureMetrics = True | Mechanism: Tracks and reports failures when publishing packages. | Purpose: Helps developers understand and fix issues when uploading game assets.
- FFlagSQLiteCacheFixContains = True | Mechanism: Fixes issues with how cached data is checked in the SQLite database. | Purpose: Enhances game performance by ensuring data is retrieved more reliably.
- FFlagSQLiteCacheFixName = True | Mechanism: Fixes naming issues in the SQLite cache system for data storage. | Purpose: Ensures more reliable data retrieval, leading to fewer errors and a smoother gameplay experience.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 1caa745e5184f77d81912d83763a517ef36fa461 to ab78fe8e4d722b6661bd4229ae1d08c2417ef544 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 19:50:17 to 01/21/2026 19:57:04 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 1caa745e5184f77d81912d83763a517ef36fa461 to ab78fe8e4d722b6661bd4229ae1d08c2417ef544 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 19:50:17 to 01/21/2026 19:57:04 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagAndroidHevcEncoderCheck_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:49:46) | Mechanism: Checks if the Android device supports HEVC encoding for better video quality. | Purpose: Improves video streaming quality on supported Android devices.
- FFlagEnablePackagePublishFailureMetrics_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:53:14) | Mechanism: Tracks and reports errors when users try to publish packages. | Purpose: Helps developers understand and fix issues when publishing their content.
- FFlagSQLiteCacheFixContains_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:55:13) | Mechanism: Fixes issues with the caching system in the database. | Purpose: Enhances game performance by reducing loading times.
- FFlagSQLiteCacheFixName_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:54:43) | Mechanism: Fixes issues with how data is stored and retrieved in the SQLite database. | Purpose: Improves game performance by ensuring data is accessed more reliably.

## b770bfbde - 2026-01-21 13:51:49 -0600 - 01/21/2026 13:51:49
Added in Other:
- FFlagDevConsoleDownArrowIconFix_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T19:48:10 | Mechanism: Fixes the icon display for the down arrow in the developer console. | Purpose: Improves the visual clarity of the developer console for better usability.
- FFlagExplorerHeartbeatTelemetry_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T19:49:24 | Mechanism: Collects data on the performance of the Explorer tool in real-time. | Purpose: Helps improve the Explorer tool's performance and reliability for developers.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from fa4a761c6c4e4257e25d846094082d965a03fac9 to 1caa745e5184f77d81912d83763a517ef36fa461 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 19:46:54 to 01/21/2026 19:50:17 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from fa4a761c6c4e4257e25d846094082d965a03fac9 to 1caa745e5184f77d81912d83763a517ef36fa461 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 19:46:54 to 01/21/2026 19:50:17 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## fb49c0f3d - 2026-01-21 13:49:31 -0600 - 01/21/2026 13:49:30
Added in Network:
- FFlagAudioDeviceInputFixReplicationChecks = True | Mechanism: Fixes checks for audio input devices. | Purpose: Improves audio quality and reliability for players using input devices.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 45f3432bb752326ba163530b20af8eeb079ab5c1 to fa4a761c6c4e4257e25d846094082d965a03fac9 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 19:46:33 to 01/21/2026 19:46:54 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 45f3432bb752326ba163530b20af8eeb079ab5c1 to fa4a761c6c4e4257e25d846094082d965a03fac9 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 19:46:33 to 01/21/2026 19:46:54 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Network:
- FFlagAudioDeviceInputFixReplicationChecks_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:44:20) | Mechanism: Improves checks for audio device input replication. | Purpose: Ensures better audio quality and synchronization during gameplay.

## 8664aec0f - 2026-01-21 13:47:14 -0600 - 01/21/2026 13:47:14
Added in Other:
- FFlagGImageWebPBiEndianLoad_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T19:44:39 | Mechanism: Enables loading WebP images in a specific byte order. | Purpose: Improves image loading performance for certain graphics.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from a19cd15e7116a3ab7ec5f0756a85b0f714fe47f5 to 45f3432bb752326ba163530b20af8eeb079ab5c1 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 19:36:39 to 01/21/2026 19:46:33 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from a19cd15e7116a3ab7ec5f0756a85b0f714fe47f5 to 45f3432bb752326ba163530b20af8eeb079ab5c1 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 19:36:39 to 01/21/2026 19:46:33 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## a5d7feab3 - 2026-01-21 13:38:21 -0600 - 01/21/2026 13:38:21
Changed in Other:
- DFIntSimAdaptiveExtraIterations changed from 4 to 6 | Mechanism: Adjusts the number of iterations in simulations based on performance needs. | Purpose: Improves the accuracy of game simulations, resulting in more realistic game mechanics for players.
- DFStringFlagRepoGitHashDynamicString changed from 2427952aa6db399364d108a7182756095478b7d6 to a19cd15e7116a3ab7ec5f0756a85b0f714fe47f5 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 19:27:17 to 01/21/2026 19:36:39 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 2427952aa6db399364d108a7182756095478b7d6 to a19cd15e7116a3ab7ec5f0756a85b0f714fe47f5 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 19:27:17 to 01/21/2026 19:36:39 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- DFIntSimAdaptiveExtraIterations_Staged removed (was 6;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:30:46) | Mechanism: Increases the number of simulation iterations for better accuracy. | Purpose: Enhances game physics and interactions for a smoother experience.

## 7f0e57dae - 2026-01-21 13:29:26 -0600 - 01/21/2026 13:29:26
Added in Other:
- FFlagAsyncLoadRvSubsystem = True | Mechanism: Enables asynchronous loading of the rendering subsystem. | Purpose: Improves game performance by allowing graphics to load without interrupting gameplay.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 1857239de133466bf4a4096616c9f19a6cc0914d to 2427952aa6db399364d108a7182756095478b7d6 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 19:23:38 to 01/21/2026 19:27:17 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 1857239de133466bf4a4096616c9f19a6cc0914d to 2427952aa6db399364d108a7182756095478b7d6 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 19:23:38 to 01/21/2026 19:27:17 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagAsyncLoadRvSubsystem_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:24:00) | Mechanism: Enables asynchronous loading of certain game resources to improve performance. | Purpose: Reduces loading times and enhances the overall gaming experience.

## eddaa34f2 - 2026-01-21 13:24:46 -0600 - 01/21/2026 13:24:45
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from cc7a70df98f091a927b298b3ffe0870778e5d114 to 1857239de133466bf4a4096616c9f19a6cc0914d | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 19:21:48 to 01/21/2026 19:23:38 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from cc7a70df98f091a927b298b3ffe0870778e5d114 to 1857239de133466bf4a4096616c9f19a6cc0914d | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 19:21:48 to 01/21/2026 19:23:38 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 8b6096fae - 2026-01-21 13:22:28 -0600 - 01/21/2026 13:22:27
Added in Other:
- FFlagAXFixHydratedWidgetsParams2 = True | Mechanism: Fixes issues with widget parameters in the user interface. | Purpose: Improves the stability and appearance of UI elements for players.
- FFlagAXHandleCategoryIdsTaxonomyDeepLinks_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T19:19:47 | Mechanism: Improves how category links are managed for game content. | Purpose: Enhances navigation for players by making it easier to find specific game categories.
- FIntCoreScriptsProfilerSamplingHundredthsPercent = 1000 | Mechanism: Changes how often performance data is collected for core scripts. | Purpose: Helps developers optimize game performance by providing more accurate profiling data.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from f078a89788194daa9afc916b58666cade10e7608 to cc7a70df98f091a927b298b3ffe0870778e5d114 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 19:17:21 to 01/21/2026 19:21:48 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from f078a89788194daa9afc916b58666cade10e7608 to cc7a70df98f091a927b298b3ffe0870778e5d114 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 19:17:21 to 01/21/2026 19:21:48 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagAXFixHydratedWidgetsParams2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:18:55) | Mechanism: Fixes issues with widget parameters in the AX system. | Purpose: Improves the stability and performance of user interface widgets.
- FIntCoreScriptsProfilerSamplingHundredthsPercent_Staged removed (was 1000;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:17:45) | Mechanism: Adjusts the sampling rate for performance tracking of core scripts. | Purpose: Helps developers optimize game performance, leading to smoother gameplay for players.

## 3f1b31db7 - 2026-01-21 13:20:10 -0600 - 01/21/2026 13:20:10
Added in Other:
- DFFlagRM3ScreenshotEncoding = True | Mechanism: Changes the way screenshots are encoded for storage. | Purpose: Enhances image quality and reduces file size for player screenshots.
- FFlagACSUGCValidationRCCOnly = True | Mechanism: Restricts user-generated content validation to a specific method. | Purpose: Ensures that only approved content is used, improving game safety and quality.
- FFlagStylingCachedPropertiesConst = True | Mechanism: Optimizes how styling properties are cached for faster access. | Purpose: Improves the visual performance of games, making them load and run smoother.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from fafd11a4ac363503a1ffe304f3c74e4066edd928 to f078a89788194daa9afc916b58666cade10e7608 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 19:15:11 to 01/21/2026 19:17:21 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from fafd11a4ac363503a1ffe304f3c74e4066edd928 to f078a89788194daa9afc916b58666cade10e7608 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 19:15:11 to 01/21/2026 19:17:21 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- DFFlagRM3ScreenshotEncoding_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:07:33) | Mechanism: Implements a new method for encoding screenshots taken in the game. | Purpose: Improves the quality and efficiency of screenshots for players.
- FFlagACSUGCValidationRCCOnly_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:09:21) | Mechanism: Restricts UGC validation to specific criteria within the RCC system. | Purpose: Ensures that user-generated content meets certain standards for quality and safety.
- FFlagStylingCachedPropertiesConst_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:14:13) | Mechanism: Enhances the way styling properties are stored and reused. | Purpose: Makes games look better and load faster by optimizing visual elements.

## eebd2ecf8 - 2026-01-21 13:17:53 -0600 - 01/21/2026 13:17:53
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 1702448c135fd17f87ff607112cc9ebbe71262fd to fafd11a4ac363503a1ffe304f3c74e4066edd928 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 19:01:59 to 01/21/2026 19:15:11 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 1702448c135fd17f87ff607112cc9ebbe71262fd to fafd11a4ac363503a1ffe304f3c74e4066edd928 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 19:01:59 to 01/21/2026 19:15:11 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## 61a48c0d9 - 2026-01-21 13:04:27 -0600 - 01/21/2026 13:04:26
Added in Other:
- FFlagAddDisableHangReportingOnDebuggerBreak2 = True | Mechanism: Disables reporting of hangs when the debugger is paused. | Purpose: Improves debugging experience by reducing unnecessary reports during pauses.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 425396dc5eb690b0153fa63cd957b122cb02f544 to 1702448c135fd17f87ff607112cc9ebbe71262fd | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 18:59:22 to 01/21/2026 19:01:59 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 425396dc5eb690b0153fa63cd957b122cb02f544 to 1702448c135fd17f87ff607112cc9ebbe71262fd | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 18:59:22 to 01/21/2026 19:01:59 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagAddDisableHangReportingOnDebuggerBreak2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T17:57:41) | Mechanism: Allows developers to turn off hang reporting when the debugger is paused. | Purpose: Reduces unnecessary alerts for developers when they are debugging their code.

## 187decc55 - 2026-01-21 13:02:08 -0600 - 01/21/2026 13:02:08
Added in Other:
- FFlagPerformanceControlBudgetSystemRollout10_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:58:31 | Mechanism: Introduces a new system to manage performance budgets. | Purpose: Optimizes game performance, leading to smoother gameplay for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from d90a19fd523b0680014657217d26268d2f92a1df to 425396dc5eb690b0153fa63cd957b122cb02f544 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 18:56:58 to 01/21/2026 18:59:22 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from d90a19fd523b0680014657217d26268d2f92a1df to 425396dc5eb690b0153fa63cd957b122cb02f544 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 18:56:58 to 01/21/2026 18:59:22 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.

## fac4e58c0 - 2026-01-21 12:57:34 -0600 - 01/21/2026 12:57:34
Added in Other:
- FFlagSQLiteCacheFixContains_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:55:13 | Mechanism: Fixes issues with the caching system in the database. | Purpose: Enhances game performance by reducing loading times.
- FFlagSQLiteCacheFixName_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:54:43 | Mechanism: Fixes issues with how data is stored and retrieved in the SQLite database. | Purpose: Improves game performance by ensuring data is accessed more reliably.
- FFlagSupportTerminalMilestoneInReactProfilerLogger = True | Mechanism: Enhances logging capabilities in the React Profiler for terminal milestones. | Purpose: Improves performance tracking and debugging for developers.
- FFlagTelemetryCacheTrackBytes = True | Mechanism: Tracks the amount of data used in telemetry caching. | Purpose: Helps optimize data usage and improve performance monitoring.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from e944c19dc8e28f6c979a766754ad4a008a433008 to d90a19fd523b0680014657217d26268d2f92a1df | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 18:54:11 to 01/21/2026 18:56:58 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from e944c19dc8e28f6c979a766754ad4a008a433008 to d90a19fd523b0680014657217d26268d2f92a1df | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 18:54:11 to 01/21/2026 18:56:58 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagSupportTerminalMilestoneInReactProfilerLogger_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T17:50:54) | Mechanism: Integrates terminal milestones into the React Profiler for better performance tracking. | Purpose: Helps developers optimize game performance, leading to smoother gameplay for players.
- FFlagTelemetryCacheTrackBytes_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T17:50:57) | Mechanism: Tracks the amount of data used by telemetry features. | Purpose: Helps developers optimize performance and reduce data usage for players.

## 32570e96b - 2026-01-21 12:55:17 -0600 - 01/21/2026 12:55:17
Added in Other:
- FFlagAddVideoDetectorWrapper = True | Mechanism: Introduces a new layer for detecting video content. | Purpose: Enhances content moderation by improving video detection capabilities.
- FFlagEnablePackagePublishFailureMetrics_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:53:14 | Mechanism: Tracks and reports errors when users try to publish packages. | Purpose: Helps developers understand and fix issues when publishing their content.
Added in Camera/UI:
- FFlagRemoveExperienceMenuABTestManager = True | Mechanism: Removes the A/B testing manager for the experience menu. | Purpose: Streamlines the experience menu for all players by eliminating experimental features.
- FFlagSduiBadgeTileContained = True | Mechanism: Changes how badge tiles are displayed in the UI. | Purpose: Makes badge displays more visually appealing and organized for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 572d649795d0ff8e9ce79cbaf76853c04a844ee2 to e944c19dc8e28f6c979a766754ad4a008a433008 | Mechanism: Uses a dynamic string for the Git hash in the repository. | Purpose: Ensures players always have the latest version information for better performance.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 18:51:02 to 01/21/2026 18:54:11 | Mechanism: Modifies how dynamic strings display timestamps. | Purpose: Improves the readability and presentation of timestamps for players.
- FStringFlagRepoGitHashFastString changed from 572d649795d0ff8e9ce79cbaf76853c04a844ee2 to e944c19dc8e28f6c979a766754ad4a008a433008 | Mechanism: Links to a specific version of the code repository. | Purpose: Ensures stability by using a consistent code version for features.
- FStringFlipTimeStampFastString changed from 01/21/2026 18:51:02 to 01/21/2026 18:54:11 | Mechanism: Enhances the speed of processing timestamp strings. | Purpose: Makes time-related functions faster for better gameplay experience.
Removed in Other:
- FFlagAddVideoDetectorWrapper_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T17:47:06) | Mechanism: Introduces a wrapper for detecting videos in a staged environment. | Purpose: Allows for better handling of video content in games, improving user experience.
Removed in Camera/UI:
- FFlagRemoveExperienceMenuABTestManager_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;70130128;2026-01-21T17:46:08) | Mechanism: Disables a feature that tests different versions of the experience menu. | Purpose: Streamlines the user interface by removing unnecessary testing features, leading to a cleaner experience.
- FFlagSduiBadgeTileContained_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;308554894;2026-01-21T17:47:00) | Mechanism: Enables badge tiles to be contained within a specific UI element. | Purpose: Improves the organization and presentation of badge information in the user interface.