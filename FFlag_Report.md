# Roblox Client FFlag Intel Report (350 Days)

- Last Run: 2026-01-22 09:51:31 AM PST
- Flags Added: 234
- Flags Changed: 825
- Flags Removed: 142

## Summary
| Category | Added | Changed | Removed | Total |
|---|---|---|---|---|
| Graphics | 6 | 0 | 3 | 9 |
| Physics | 1 | 0 | 1 | 2 |
| Network | 15 | 1 | 9 | 25 |
| Camera/UI | 21 | 3 | 11 | 35 |
| Security | 0 | 0 | 0 | 0 |
| World | 0 | 0 | 0 | 0 |
| Input | 2 | 0 | 1 | 3 |
| Hit | 0 | 0 | 0 | 0 |
| Interpolation | 0 | 0 | 0 | 0 |
| Body | 0 | 0 | 0 | 0 |
| Other | 189 | 821 | 117 | 1127 |

## History Summary

- Total Historical Added: 234
- Total Historical Changed: 825
- Total Historical Removed: 142
- Note: Limited history available.

## bce950d55 - 2026-01-21 19:32:54 -0600 - 01/21/2026 19:32:53
Added in Other:
- FFlagEnableHttpStreamingForMsxml = True | Mechanism: Allows streaming of data over HTTP using a specific method. | Purpose: Enhances the speed and reliability of loading game assets.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from c3af12d56b29e32441da8b97e9b0fe0a74aeeb30 to 4fc2dc7b50d91aef4b82cb35623e2d628208687a | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 01:11:45 to 01/22/2026 01:31:40 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from c3af12d56b29e32441da8b97e9b0fe0a74aeeb30 to 4fc2dc7b50d91aef4b82cb35623e2d628208687a | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/22/2026 01:11:45 to 01/22/2026 01:31:40 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagEnableHttpStreamingForMsxml_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T00:30:04) | Mechanism: Enables streaming of data over HTTP for certain features. | Purpose: Improves performance and responsiveness of game features.

## 787a760b1 - 2026-01-21 19:12:53 -0600 - 01/21/2026 19:12:53
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 7f04efbeb9e18b3d49336d03c05d56fd39696f2a to c3af12d56b29e32441da8b97e9b0fe0a74aeeb30 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 01:02:29 to 01/22/2026 01:11:45 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 7f04efbeb9e18b3d49336d03c05d56fd39696f2a to c3af12d56b29e32441da8b97e9b0fe0a74aeeb30 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/22/2026 01:02:29 to 01/22/2026 01:11:45 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 417161f1e - 2026-01-21 19:04:01 -0600 - 01/21/2026 19:04:01
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from d276764fc7da76e83e0f7ceabc34d99f92f39aee to 7f04efbeb9e18b3d49336d03c05d56fd39696f2a | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 00:56:38 to 01/22/2026 01:02:29 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from d276764fc7da76e83e0f7ceabc34d99f92f39aee to 7f04efbeb9e18b3d49336d03c05d56fd39696f2a | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/22/2026 00:56:38 to 01/22/2026 01:02:29 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Changed in Camera/UI:
- FFlagAvatarAnimationCameraZoom changed from True to False | Mechanism: Changes how the camera zooms during avatar animations. | Purpose: Enhances the visual experience of avatar movements.
Removed in Camera/UI:
- FFlagAvatarAnimationCameraZoom_Staged removed (was false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;1122964870;2026-01-21T23:59:49) | Mechanism: Introduces a zoom feature for the camera during avatar animations. | Purpose: Enhances the visual experience of animations, making them more engaging for players.

## 99ada3ad5 - 2026-01-21 18:57:18 -0600 - 01/21/2026 18:57:17
Added in Network:
- DFFlagFixTeleportToReservedServerHang = True | Mechanism: Fixes a bug that causes delays when teleporting to reserved servers. | Purpose: Ensures smoother and faster transitions for players joining reserved servers.
- DFFlagFixTeleportToReservedServerPlayerHang = True | Mechanism: Fixes an issue where players would get stuck when teleporting to reserved servers. | Purpose: Ensures smoother transitions for players when moving between game servers.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 41587942bbf4e6f9726bf23ffbb3e2059c6d48f9 to d276764fc7da76e83e0f7ceabc34d99f92f39aee | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 00:51:59 to 01/22/2026 00:56:38 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 41587942bbf4e6f9726bf23ffbb3e2059c6d48f9 to d276764fc7da76e83e0f7ceabc34d99f92f39aee | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/22/2026 00:51:59 to 01/22/2026 00:56:38 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Network:
- DFFlagFixTeleportToReservedServerHang_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:54:42) | Mechanism: Fixes issues with players getting stuck when trying to teleport to reserved servers. | Purpose: Ensures smoother gameplay by allowing players to teleport without problems.
- DFFlagFixTeleportToReservedServerPlayerHang_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:52:43) | Mechanism: Fixes a bug that caused players to get stuck when teleporting to reserved servers. | Purpose: Ensures a smoother experience for players when joining specific game servers.

## 67a02bda4 - 2026-01-21 18:52:43 -0600 - 01/21/2026 18:52:43
Added in Other:
- FFlagInExperienceRequestProfileSettings_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T00:48:55 | Mechanism: Introduces a new way to request player profile settings within games. | Purpose: Enhances player customization options and settings management in experiences.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 2e25b071909ec16fd2698830c6ecf09064b44fa1 to 41587942bbf4e6f9726bf23ffbb3e2059c6d48f9 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 00:46:53 to 01/22/2026 00:51:59 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 2e25b071909ec16fd2698830c6ecf09064b44fa1 to 41587942bbf4e6f9726bf23ffbb3e2059c6d48f9 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/22/2026 00:46:53 to 01/22/2026 00:51:59 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 29521f583 - 2026-01-21 18:48:09 -0600 - 01/21/2026 18:48:09
Added in Camera/UI:
- FFlagFixMoreSubMenuTitleFlash = True | Mechanism: Fixes the flashing issue in submenu titles for better visibility. | Purpose: Makes it easier for players to read menu titles without distractions.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 5be446d544a53871d3ac2a3a40e67d412b606ccc to 2e25b071909ec16fd2698830c6ecf09064b44fa1 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 00:30:56 to 01/22/2026 00:46:53 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 5be446d544a53871d3ac2a3a40e67d412b606ccc to 2e25b071909ec16fd2698830c6ecf09064b44fa1 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/22/2026 00:30:56 to 01/22/2026 00:46:53 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Camera/UI:
- FFlagFixMoreSubMenuTitleFlash_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:42:58) | Mechanism: Addresses issues with flashing titles in submenus. | Purpose: Improves the user interface by making it more visually stable and pleasant.

## becf90185 - 2026-01-21 18:32:41 -0600 - 01/21/2026 18:32:41
Added in Other:
- FFlagEnableHttpStreamingForMsxml_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-22T00:30:04 | Mechanism: Enables streaming of data over HTTP for certain features. | Purpose: Improves performance and responsiveness of game features.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from d156c1cedb8791c6246ef9dd5e45c16d87bf80c5 to 5be446d544a53871d3ac2a3a40e67d412b606ccc | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 00:27:18 to 01/22/2026 00:30:56 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from d156c1cedb8791c6246ef9dd5e45c16d87bf80c5 to 5be446d544a53871d3ac2a3a40e67d412b606ccc | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/22/2026 00:27:18 to 01/22/2026 00:30:56 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## d4217dd81 - 2026-01-21 18:28:12 -0600 - 01/21/2026 18:28:12
Added in Other:
- FFlagEnableRewardedAdFormatExperiment = True | Mechanism: Enables a new format for displaying rewarded ads in games. | Purpose: Players can earn rewards by watching ads, enhancing their gaming experience.
- FFlagPassAdUnitToNativeAndroid = True | Mechanism: Allows ad units to be passed directly to the native Android app. | Purpose: Enhances ad display and revenue generation on Android devices.
- FFlagSendRewardedVideoExperimentVariantAndAdUnitIdToNative2 = True | Mechanism: Sends specific data about video ads to the native system. | Purpose: Improves the experience and rewards for players watching ads in games.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from da26789b12b7bd8376a537646b7381436a1b8728 to d156c1cedb8791c6246ef9dd5e45c16d87bf80c5 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 00:21:56 to 01/22/2026 00:27:18 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from da26789b12b7bd8376a537646b7381436a1b8728 to d156c1cedb8791c6246ef9dd5e45c16d87bf80c5 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/22/2026 00:21:56 to 01/22/2026 00:27:18 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagEnableRewardedAdFormatExperiment_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;2028022506;2026-01-21T23:21:48) | Mechanism: Introduces a new format for displaying rewarded advertisements in games. | Purpose: Allows players to earn rewards by watching ads, enhancing engagement and monetization.
- FFlagPassAdUnitToNativeAndroid_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;2028022506;2026-01-21T23:21:48) | Mechanism: Enables passing ad unit information to the native Android app. | Purpose: Improves ad performance and relevance for players using the Android app.
- FFlagSendRewardedVideoExperimentVariantAndAdUnitIdToNative2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;2028022506;2026-01-21T23:21:48) | Mechanism: Sends specific data about video ads to the native platform for better tracking. | Purpose: Enhances the experience of rewarded video ads, potentially offering better rewards for players.

## 4c6a2d5a3 - 2026-01-21 18:23:40 -0600 - 01/21/2026 18:23:40
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from ead87777d27124b06e6f5be6d3783dd1015bdac5 to da26789b12b7bd8376a537646b7381436a1b8728 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 00:17:28 to 01/22/2026 00:21:56 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from ead87777d27124b06e6f5be6d3783dd1015bdac5 to da26789b12b7bd8376a537646b7381436a1b8728 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/22/2026 00:17:28 to 01/22/2026 00:21:56 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 9a8415808 - 2026-01-21 18:19:12 -0600 - 01/21/2026 18:19:12
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from e304719ff0f58c7b2dedbc0d7b2acd819833492f to ead87777d27124b06e6f5be6d3783dd1015bdac5 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 00:12:07 to 01/22/2026 00:17:28 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FFlagExplorerHeartbeatTelemetry changed from True to False | Mechanism: Tracks and reports the activity of the Explorer tool in real-time. | Purpose: Helps developers understand how players use the Explorer, leading to better tools.
- FStringFlagRepoGitHashFastString changed from e304719ff0f58c7b2dedbc0d7b2acd819833492f to ead87777d27124b06e6f5be6d3783dd1015bdac5 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/22/2026 00:12:07 to 01/22/2026 00:17:28 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagExplorerHeartbeatTelemetry_Staged removed (was false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:11:01) | Mechanism: Tracks the performance of the Explorer tool in real-time. | Purpose: Ensures the Explorer tool runs efficiently, improving the development experience for creators.

## 3808f1a95 - 2026-01-21 18:14:42 -0600 - 01/21/2026 18:14:42
Added in Other:
- DFFlagMathUseNewReflection2 = True | Mechanism: Updates the math functions to use a new reflection system for better accuracy. | Purpose: Enhances the precision of mathematical calculations in games, improving gameplay mechanics.
- DFFlagSimCSG3EnableNewAPIPluginUse2 = True | Mechanism: Enables a new API for plugins that work with CSG (Constructive Solid Geometry). | Purpose: Allows developers to create more advanced building tools.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 7e358cdff52250f1285194dbaf7dbecc476a3683 to e304719ff0f58c7b2dedbc0d7b2acd819833492f | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 00:07:42 to 01/22/2026 00:12:07 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 7e358cdff52250f1285194dbaf7dbecc476a3683 to e304719ff0f58c7b2dedbc0d7b2acd819833492f | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/22/2026 00:07:42 to 01/22/2026 00:12:07 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagMathUseNewReflection2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:09:58) | Mechanism: Switches to a new method for mathematical calculations in scripts. | Purpose: Enhances the accuracy and efficiency of math operations in games.
- DFFlagSimCSG3EnableNewAPIPluginUse2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:09:06) | Mechanism: Enables a new API for plugins related to CSG (Constructive Solid Geometry). | Purpose: Gives developers better tools to create complex shapes, enhancing game design.

## 9a8352c74 - 2026-01-21 18:10:11 -0600 - 01/21/2026 18:10:11
Added in Other:
- FFlagCaptureServiceEnableTakeCaptureApi2 = True | Mechanism: Enables a new API for capturing game states. | Purpose: Allows developers to create better snapshots of game states for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 055fb5e03ba54e044a347f2748a92740e58495a6 to 7e358cdff52250f1285194dbaf7dbecc476a3683 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 00:06:13 to 01/22/2026 00:07:42 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 055fb5e03ba54e044a347f2748a92740e58495a6 to 7e358cdff52250f1285194dbaf7dbecc476a3683 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/22/2026 00:06:13 to 01/22/2026 00:07:42 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagCaptureServiceEnableTakeCaptureApi2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:02:54) | Mechanism: Enables a new API for capturing game states or screenshots. | Purpose: Allows players to easily capture and share their gameplay experiences.

## 9ba543334 - 2026-01-21 18:07:56 -0600 - 01/21/2026 18:07:55
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 56a49c980d9a6af659dc2fb741ff3c0ef3d7f645 to 055fb5e03ba54e044a347f2748a92740e58495a6 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/22/2026 00:01:03 to 01/22/2026 00:06:13 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 56a49c980d9a6af659dc2fb741ff3c0ef3d7f645 to 055fb5e03ba54e044a347f2748a92740e58495a6 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/22/2026 00:01:03 to 01/22/2026 00:06:13 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 88d1f3e76 - 2026-01-21 18:03:17 -0600 - 01/21/2026 18:03:17
Added in Camera/UI:
- FFlagAvatarAnimationCameraZoom_Staged = false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;1122964870;2026-01-21T23:59:49 | Mechanism: Introduces a zoom feature for the camera during avatar animations. | Purpose: Enhances the visual experience of animations, making them more engaging for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from e58337c29e49e81e38600507b08d02e584ee6709 to 56a49c980d9a6af659dc2fb741ff3c0ef3d7f645 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 23:57:21 to 01/22/2026 00:01:03 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from e58337c29e49e81e38600507b08d02e584ee6709 to 56a49c980d9a6af659dc2fb741ff3c0ef3d7f645 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 23:57:21 to 01/22/2026 00:01:03 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 507b92d4c - 2026-01-21 17:58:47 -0600 - 01/21/2026 17:58:47
Added in Other:
- DFFlagEnableSystrayExpEnrollment = True | Mechanism: Enables a system tray icon for easier access to experiences. | Purpose: Allows players to quickly access and manage their Roblox experiences from their desktop.
- FFlagAmrFixCustomizeGroups = True | Mechanism: Fixes issues related to customizing group settings and features. | Purpose: Enhances the user experience for group management and customization.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from c2f964affed08f6cafdcb745960403916b39b973 to e58337c29e49e81e38600507b08d02e584ee6709 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 23:55:36 to 01/21/2026 23:57:21 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from c2f964affed08f6cafdcb745960403916b39b973 to e58337c29e49e81e38600507b08d02e584ee6709 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 23:55:36 to 01/21/2026 23:57:21 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagEnableSystrayExpEnrollment_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:53:30) | Mechanism: Enables a new feature in the system tray for user enrollment in experiments. | Purpose: Allows players to participate in new features and improvements more easily.
- FFlagAmrFixCustomizeGroups_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;1964796395;2026-01-21T22:51:36) | Mechanism: Fixes issues related to customizing group settings and features. | Purpose: Enhances the ability for players to personalize their groups effectively.

## c6d0101a6 - 2026-01-21 17:56:31 -0600 - 01/21/2026 17:56:31
Added in Network:
- DFFlagFixTeleportToReservedServerHang_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:54:42 | Mechanism: Fixes issues with players getting stuck when trying to teleport to reserved servers. | Purpose: Ensures smoother gameplay by allowing players to teleport without problems.
- DFFlagFixTeleportToReservedServerPlayerHang_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:52:43 | Mechanism: Fixes a bug that caused players to get stuck when teleporting to reserved servers. | Purpose: Ensures a smoother experience for players when joining specific game servers.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from a6bc744c1a36205210d284808360bee295b541f6 to c2f964affed08f6cafdcb745960403916b39b973 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 23:51:42 to 01/21/2026 23:55:36 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from a6bc744c1a36205210d284808360bee295b541f6 to c2f964affed08f6cafdcb745960403916b39b973 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 23:51:42 to 01/21/2026 23:55:36 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## bbc7fd9a9 - 2026-01-21 17:54:15 -0600 - 01/21/2026 17:54:14
Added in Other:
- DFFlagEnableSystrayBackgroundAppUpdate = True | Mechanism: Allows the Roblox app to update in the background without interrupting the user. | Purpose: Ensures players always have the latest version without needing to manually update.
- DFIntSystrayEventsThrottleHundredthsPercent = 10000 | Mechanism: Limits the frequency of system tray events to reduce overload. | Purpose: Enhances performance by preventing too many notifications at once.
- FFlagSystemTrayDeviceSettings2 = True | Mechanism: Updates the system tray settings for devices in Roblox. | Purpose: Improves user experience by providing better access to device settings.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from cdd8a37756a41e5713345a5bf6d3874d9ffe3305 to a6bc744c1a36205210d284808360bee295b541f6 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 23:51:04 to 01/21/2026 23:51:42 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from cdd8a37756a41e5713345a5bf6d3874d9ffe3305 to a6bc744c1a36205210d284808360bee295b541f6 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 23:51:04 to 01/21/2026 23:51:42 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagEnableSystrayBackgroundAppUpdate_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:50:10) | Mechanism: Allows background updates for the Roblox app through the system tray. | Purpose: Keeps the Roblox app up-to-date without interrupting the user's experience.
- DFIntSystrayEventsThrottleHundredthsPercent_Staged removed (was 10000;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:46:36) | Mechanism: Limits the frequency of system tray events to reduce overload. | Purpose: Improves responsiveness and reduces lag during gameplay.
- FFlagSystemTrayDeviceSettings2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:47:38) | Mechanism: Updates the system tray to include new device settings options. | Purpose: Allows players to easily adjust their device settings for a better gaming experience.

## 81b588b9d - 2026-01-21 17:51:57 -0600 - 01/21/2026 17:51:57
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from f5b99c00682fd74ee980739e7d697cb0571001f1 to cdd8a37756a41e5713345a5bf6d3874d9ffe3305 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 23:47:15 to 01/21/2026 23:51:04 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from f5b99c00682fd74ee980739e7d697cb0571001f1 to cdd8a37756a41e5713345a5bf6d3874d9ffe3305 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 23:47:15 to 01/21/2026 23:51:04 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 2624d2bbc - 2026-01-21 17:49:42 -0600 - 01/21/2026 17:49:41
Added in Other:
- DFFlagRemoveTrayUserAgentKeyword = True | Mechanism: Removes specific keywords from the user agent string sent by the app. | Purpose: Enhances privacy by not disclosing certain information about the user's device.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from e93f0d569677281931d803b5445b009020f11433 to f5b99c00682fd74ee980739e7d697cb0571001f1 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 23:44:49 to 01/21/2026 23:47:15 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from e93f0d569677281931d803b5445b009020f11433 to f5b99c00682fd74ee980739e7d697cb0571001f1 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 23:44:49 to 01/21/2026 23:47:15 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagRemoveTrayUserAgentKeyword_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:45:24) | Mechanism: Removes specific keywords from the user agent string in the tray. | Purpose: Improves privacy and reduces unnecessary data sharing for players.

## 98b23afa2 - 2026-01-21 17:47:24 -0600 - 01/21/2026 17:47:24
Added in Camera/UI:
- FFlagFixMoreSubMenuTitleFlash_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:42:58 | Mechanism: Addresses issues with flashing titles in submenus. | Purpose: Improves the user interface by making it more visually stable and pleasant.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 38a9fdf126a09509db576091ef227c2465294f96 to e93f0d569677281931d803b5445b009020f11433 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 23:27:10 to 01/21/2026 23:44:49 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 38a9fdf126a09509db576091ef227c2465294f96 to e93f0d569677281931d803b5445b009020f11433 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 23:27:10 to 01/21/2026 23:44:49 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 715b6d898 - 2026-01-21 17:29:42 -0600 - 01/21/2026 17:29:41
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from fe9d54586cddab42e8b0bd3e5e4ebf7cbb9bb506 to 38a9fdf126a09509db576091ef227c2465294f96 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 23:23:45 to 01/21/2026 23:27:10 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FFlagLuaAppGameTileWideVideoThumbnail changed from True to False | Mechanism: Enables wider video thumbnails for game tiles in the app. | Purpose: Enhances visual appeal and engagement by showcasing game videos more effectively.
- FStringFlagRepoGitHashFastString changed from fe9d54586cddab42e8b0bd3e5e4ebf7cbb9bb506 to 38a9fdf126a09509db576091ef227c2465294f96 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 23:23:45 to 01/21/2026 23:27:10 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagLuaAppGameTileWideVideoThumbnail_Staged removed (was false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:25:00) | Mechanism: Enables wider video thumbnails for game tiles in the Lua app. | Purpose: Provides a more visually appealing and engaging preview of games.

## 20d7cf1ef - 2026-01-21 17:25:10 -0600 - 01/21/2026 17:25:09
Added in Other:
- DFFlagUseCompletedRadiusFunc = True | Mechanism: Uses a function to determine the radius of completed tasks. | Purpose: Improves the accuracy of task completion indicators for players.
- FFlagEnableRewardedAdFormatExperiment_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;2028022506;2026-01-21T23:21:48 | Mechanism: Introduces a new format for displaying rewarded advertisements in games. | Purpose: Allows players to earn rewards by watching ads, enhancing engagement and monetization.
- FFlagPassAdUnitToNativeAndroid_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;2028022506;2026-01-21T23:21:48 | Mechanism: Enables passing ad unit information to the native Android app. | Purpose: Improves ad performance and relevance for players using the Android app.
- FFlagSendRewardedVideoExperimentVariantAndAdUnitIdToNative2_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;2028022506;2026-01-21T23:21:48 | Mechanism: Sends specific data about video ads to the native platform for better tracking. | Purpose: Enhances the experience of rewarded video ads, potentially offering better rewards for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 335bc44fc6a4ba540416f7af5640246f50d78103 to fe9d54586cddab42e8b0bd3e5e4ebf7cbb9bb506 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 23:19:27 to 01/21/2026 23:23:45 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 335bc44fc6a4ba540416f7af5640246f50d78103 to fe9d54586cddab42e8b0bd3e5e4ebf7cbb9bb506 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 23:19:27 to 01/21/2026 23:23:45 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagUseCompletedRadiusFunc_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:18:16) | Mechanism: Implements a new function for calculating distances in game environments. | Purpose: Players experience improved gameplay mechanics related to distance and interaction.

## 14a7e3774 - 2026-01-21 17:20:34 -0600 - 01/21/2026 17:20:34
Added in Other:
- DFFlagCLI184446 = True | Mechanism: Activates a specific command line interface feature for developers. | Purpose: Enhances developer tools for better game management and debugging.
- FFlagAXScrollingListAutomaticCanvasSize = True | Mechanism: Automatically adjusts the size of the scrolling list based on its content. | Purpose: Makes it easier for developers to create lists that fit their content without manual adjustments.
Added in Camera/UI:
- FFlagAbuseReportMenuScreenshotReduceMotionFix = True | Mechanism: Addresses motion effects in the abuse report menu when taking screenshots. | Purpose: Makes it easier for players to report issues without distractions, enhancing user experience.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 855cef1e5c6e58a94532a9782bfa6e589f62135f to 335bc44fc6a4ba540416f7af5640246f50d78103 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 23:12:33 to 01/21/2026 23:19:27 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 855cef1e5c6e58a94532a9782bfa6e589f62135f to 335bc44fc6a4ba540416f7af5640246f50d78103 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 23:12:33 to 01/21/2026 23:19:27 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagCLI184446_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:12:37) | Mechanism: Enables a new command line interface feature for developers. | Purpose: Improves the development experience by providing better tools for creating games.
- FFlagAXScrollingListAutomaticCanvasSize_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:11:33) | Mechanism: Automatically adjusts the canvas size of scrolling lists. | Purpose: Enhances user experience by ensuring all items are visible without manual adjustments.
Removed in Camera/UI:
- FFlagAbuseReportMenuScreenshotReduceMotionFix_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:13:20) | Mechanism: Reduces motion effects in the abuse report menu for smoother screenshots. | Purpose: Helps players take clearer screenshots when reporting issues.

## 7939ec87e - 2026-01-21 17:13:53 -0600 - 01/21/2026 17:13:53
Added in Other:
- DFFlagMathUseNewReflection2_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:09:58 | Mechanism: Switches to a new method for mathematical calculations in scripts. | Purpose: Enhances the accuracy and efficiency of math operations in games.
- DFFlagSimCSG3EnableNewAPIPluginUse2_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:09:06 | Mechanism: Enables a new API for plugins related to CSG (Constructive Solid Geometry). | Purpose: Gives developers better tools to create complex shapes, enhancing game design.
- FFlagExplorerHeartbeatTelemetry_Staged = false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:11:01 | Mechanism: Tracks the performance of the Explorer tool in real-time. | Purpose: Ensures the Explorer tool runs efficiently, improving the development experience for creators.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 452e2b3eaf65f91dc1b08384d4f3ae96ae270294 to 855cef1e5c6e58a94532a9782bfa6e589f62135f | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 23:04:14 to 01/21/2026 23:12:33 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 452e2b3eaf65f91dc1b08384d4f3ae96ae270294 to 855cef1e5c6e58a94532a9782bfa6e589f62135f | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 23:04:14 to 01/21/2026 23:12:33 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 052a356c5 - 2026-01-21 17:04:54 -0600 - 01/21/2026 17:04:54
Added in Other:
- FFlagCaptureServiceEnableTakeCaptureApi2_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T23:02:54 | Mechanism: Enables a new API for capturing game states or screenshots. | Purpose: Allows players to easily capture and share their gameplay experiences.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from e4a41f124952825288dd2dc170cf89025f549da6 to 452e2b3eaf65f91dc1b08384d4f3ae96ae270294 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:55:53 to 01/21/2026 23:04:14 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from e4a41f124952825288dd2dc170cf89025f549da6 to 452e2b3eaf65f91dc1b08384d4f3ae96ae270294 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:55:53 to 01/21/2026 23:04:14 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## c6e0eac80 - 2026-01-21 16:58:13 -0600 - 01/21/2026 16:58:13
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 881b91a9701d864d227d5071da3e5149609ba465 to e4a41f124952825288dd2dc170cf89025f549da6 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:54:45 to 01/21/2026 22:55:53 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 881b91a9701d864d227d5071da3e5149609ba465 to e4a41f124952825288dd2dc170cf89025f549da6 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:54:45 to 01/21/2026 22:55:53 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 8aa6ea4e1 - 2026-01-21 16:55:56 -0600 - 01/21/2026 16:55:56
Added in Other:
- DFFlagEnableSystrayExpEnrollment_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:53:30 | Mechanism: Enables a new feature in the system tray for user enrollment in experiments. | Purpose: Allows players to participate in new features and improvements more easily.
- FFlagAmrFixCustomizeGroups_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;1964796395;2026-01-21T22:51:36 | Mechanism: Fixes issues related to customizing group settings and features. | Purpose: Enhances the ability for players to personalize their groups effectively.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 25233a4d05b858a73c203143821ddd75c51ba49d to 881b91a9701d864d227d5071da3e5149609ba465 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:52:29 to 01/21/2026 22:54:45 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 25233a4d05b858a73c203143821ddd75c51ba49d to 881b91a9701d864d227d5071da3e5149609ba465 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:52:29 to 01/21/2026 22:54:45 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## f1b41ee87 - 2026-01-21 16:53:39 -0600 - 01/21/2026 16:53:39
Added in Other:
- DFFlagEnableSystrayBackgroundAppUpdate_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:50:10 | Mechanism: Allows background updates for the Roblox app through the system tray. | Purpose: Keeps the Roblox app up-to-date without interrupting the user's experience.
- DFFlagRbxStorageAvailableSpaceCreatePath = True | Mechanism: Enables the creation of paths in storage based on available space. | Purpose: Improves file management and organization for developers.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 07ebce712294862765b5e250fdf80a9d350897cc to 25233a4d05b858a73c203143821ddd75c51ba49d | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:50:31 to 01/21/2026 22:52:29 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 07ebce712294862765b5e250fdf80a9d350897cc to 25233a4d05b858a73c203143821ddd75c51ba49d | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:50:31 to 01/21/2026 22:52:29 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagRbxStorageAvailableSpaceCreatePath_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:46:36) | Mechanism: Enables a new method for checking available storage space. | Purpose: Ensures players can save their creations without running into storage issues.

## d04739481 - 2026-01-21 16:51:21 -0600 - 01/21/2026 16:51:21
Added in Other:
- FFlagSystemTrayDeviceSettings2_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:47:38 | Mechanism: Updates the system tray to include new device settings options. | Purpose: Allows players to easily adjust their device settings for a better gaming experience.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 1853aa14cf2ee474bcbb235e8fe40c7c4913e4fb to 07ebce712294862765b5e250fdf80a9d350897cc | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:47:41 to 01/21/2026 22:50:31 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 1853aa14cf2ee474bcbb235e8fe40c7c4913e4fb to 07ebce712294862765b5e250fdf80a9d350897cc | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:47:41 to 01/21/2026 22:50:31 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 8146a11cf - 2026-01-21 16:49:05 -0600 - 01/21/2026 16:49:04
Added in Other:
- DFFlagRemoveTrayUserAgentKeyword_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:45:24 | Mechanism: Removes specific keywords from the user agent string in the tray. | Purpose: Improves privacy and reduces unnecessary data sharing for players.
- DFIntSystrayEventsThrottleHundredthsPercent_Staged = 10000;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:46:36 | Mechanism: Limits the frequency of system tray events to reduce overload. | Purpose: Improves responsiveness and reduces lag during gameplay.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from cdb17f1c8ae9f948d0e2c31272cab4f083b5698c to 1853aa14cf2ee474bcbb235e8fe40c7c4913e4fb | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:37:05 to 01/21/2026 22:47:41 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from cdb17f1c8ae9f948d0e2c31272cab4f083b5698c to 1853aa14cf2ee474bcbb235e8fe40c7c4913e4fb | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:37:05 to 01/21/2026 22:47:41 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 815145c81 - 2026-01-21 16:37:50 -0600 - 01/21/2026 16:37:50
Added in Other:
- DFFlagDirectMipCalc = True | Mechanism: Calculates texture details directly for better performance. | Purpose: Improves visual quality and performance of textures in games.
Added in Graphics:
- FFlagFixFalseMipTextureFree = True | Mechanism: Corrects an issue where textures were incorrectly marked as free. | Purpose: Enhances visual quality by ensuring textures are loaded properly without unnecessary memory use.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 2845f51cd3ab4a6c077f166da8c282dc974799ad to cdb17f1c8ae9f948d0e2c31272cab4f083b5698c | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:31:49 to 01/21/2026 22:37:05 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 2845f51cd3ab4a6c077f166da8c282dc974799ad to cdb17f1c8ae9f948d0e2c31272cab4f083b5698c | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:31:49 to 01/21/2026 22:37:05 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagDirectMipCalc_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:32:06) | Mechanism: Enables direct calculation of mipmaps for textures. | Purpose: Improves texture quality and loading times in games.
Removed in Graphics:
- FFlagFixFalseMipTextureFree_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:31:28) | Mechanism: Corrects issues with texture quality at different distances. | Purpose: Improves visual clarity and reduces blurriness in textures for players.

## 0a200fb48 - 2026-01-21 16:33:21 -0600 - 01/21/2026 16:33:20
Added in Graphics:
- FFlagSharedResolutionTexture = True | Mechanism: Allows textures to be shared across different resolutions without duplication. | Purpose: Reduces memory usage and improves loading times for players by optimizing texture management.
Added in Network:
- SFFlagIAS_InstancePointersHoldAcrossReplication3 = True | Mechanism: Maintains instance pointers during data replication across servers. | Purpose: Ensures smoother gameplay by keeping track of game objects consistently, reducing bugs.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 9e37925a479ece59fc438bde3f6bc0a3f24a1234 to 2845f51cd3ab4a6c077f166da8c282dc974799ad | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:27:24 to 01/21/2026 22:31:49 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 9e37925a479ece59fc438bde3f6bc0a3f24a1234 to 2845f51cd3ab4a6c077f166da8c282dc974799ad | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:27:24 to 01/21/2026 22:31:49 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Graphics:
- FFlagSharedResolutionTexture_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:29:15) | Mechanism: Allows textures to share resolution settings across different parts of the game. | Purpose: Enhances visual consistency and performance in graphics.
Removed in Network:
- SFFlagIAS_InstancePointersHoldAcrossReplication3_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:28:00) | Mechanism: Maintains references to game objects during data updates. | Purpose: Ensures smoother gameplay and object interactions for players.

## eb9bae87c - 2026-01-21 16:28:51 -0600 - 01/21/2026 16:28:51
Added in Other:
- FFlagLuaAppGameTileWideVideoThumbnail_Staged = false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:25:00 | Mechanism: Enables wider video thumbnails for game tiles in the Lua app. | Purpose: Provides a more visually appealing and engaging preview of games.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 582a5d0cf4413e398c608d9e9bb97fa77c618606 to 9e37925a479ece59fc438bde3f6bc0a3f24a1234 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:25:07 to 01/21/2026 22:27:24 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 582a5d0cf4413e398c608d9e9bb97fa77c618606 to 9e37925a479ece59fc438bde3f6bc0a3f24a1234 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:25:07 to 01/21/2026 22:27:24 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagRM3ScreenshotEncoding_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:22:26) | Mechanism: Changes the way screenshots are encoded for better quality. | Purpose: Improves the quality of screenshots taken by players.

## b524dedc0 - 2026-01-21 16:26:34 -0600 - 01/21/2026 16:26:34
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 449630fa629f532568e01e248ba75ebbbc36abaf to 582a5d0cf4413e398c608d9e9bb97fa77c618606 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:22:17 to 01/21/2026 22:25:07 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 449630fa629f532568e01e248ba75ebbbc36abaf to 582a5d0cf4413e398c608d9e9bb97fa77c618606 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:22:17 to 01/21/2026 22:25:07 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 91a647c24 - 2026-01-21 16:24:17 -0600 - 01/21/2026 16:24:17
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from c6b23707e0f83b26f6577dd4111e50500f9fa74b to 449630fa629f532568e01e248ba75ebbbc36abaf | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:19:16 to 01/21/2026 22:22:17 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from c6b23707e0f83b26f6577dd4111e50500f9fa74b to 449630fa629f532568e01e248ba75ebbbc36abaf | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:19:16 to 01/21/2026 22:22:17 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## fa24ca6a0 - 2026-01-21 16:22:00 -0600 - 01/21/2026 16:22:00
Added in Other:
- DFFlagUseCompletedRadiusFunc_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:18:16 | Mechanism: Implements a new function for calculating distances in game environments. | Purpose: Players experience improved gameplay mechanics related to distance and interaction.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 0b9b25059d7a319b6b1b7dc82608308192524dec to c6b23707e0f83b26f6577dd4111e50500f9fa74b | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:18:02 to 01/21/2026 22:19:16 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 0b9b25059d7a319b6b1b7dc82608308192524dec to c6b23707e0f83b26f6577dd4111e50500f9fa74b | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:18:02 to 01/21/2026 22:19:16 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## b80e388c4 - 2026-01-21 16:19:44 -0600 - 01/21/2026 16:19:44
Added in Other:
- DFFlagMoveEverythingA = True | Mechanism: Enables a feature that allows all game objects to be moved more efficiently. | Purpose: Improves the overall performance and responsiveness of games.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 9e3e08638d4b22a85857a00fa7a0a11f865055f5 to 0b9b25059d7a319b6b1b7dc82608308192524dec | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:16:27 to 01/21/2026 22:18:02 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 9e3e08638d4b22a85857a00fa7a0a11f865055f5 to 0b9b25059d7a319b6b1b7dc82608308192524dec | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:16:27 to 01/21/2026 22:18:02 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagMoveEverythingA_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:13:03) | Mechanism: Allows movement of all game elements in a single operation. | Purpose: Simplifies the process of adjusting game layouts for developers.

## ec94a7a7a - 2026-01-21 16:17:26 -0600 - 01/21/2026 16:17:25
Added in Other:
- DFFlagCLI184446_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:12:37 | Mechanism: Enables a new command line interface feature for developers. | Purpose: Improves the development experience by providing better tools for creating games.
Added in Camera/UI:
- FFlagAbuseReportMenuScreenshotReduceMotionFix_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:13:20 | Mechanism: Reduces motion effects in the abuse report menu for smoother screenshots. | Purpose: Helps players take clearer screenshots when reporting issues.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 3da39ebf8e753906b7e53a482c1f160ce04a315c to 9e3e08638d4b22a85857a00fa7a0a11f865055f5 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:13:33 to 01/21/2026 22:16:27 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 3da39ebf8e753906b7e53a482c1f160ce04a315c to 9e3e08638d4b22a85857a00fa7a0a11f865055f5 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:13:33 to 01/21/2026 22:16:27 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 9703d8646 - 2026-01-21 16:15:08 -0600 - 01/21/2026 16:15:08
Added in Other:
- FFlagAXScrollingListAutomaticCanvasSize_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T22:11:33 | Mechanism: Automatically adjusts the canvas size of scrolling lists. | Purpose: Enhances user experience by ensuring all items are visible without manual adjustments.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 31f7091498c64d6a44eff7702f5f55e3f769eaf2 to 3da39ebf8e753906b7e53a482c1f160ce04a315c | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:07:36 to 01/21/2026 22:13:33 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 31f7091498c64d6a44eff7702f5f55e3f769eaf2 to 3da39ebf8e753906b7e53a482c1f160ce04a315c | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:07:36 to 01/21/2026 22:13:33 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 9959061a8 - 2026-01-21 16:08:26 -0600 - 01/21/2026 16:08:25
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 5e60fea1180cdea2dac00d067cafc332d054e396 to 31f7091498c64d6a44eff7702f5f55e3f769eaf2 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 22:02:31 to 01/21/2026 22:07:36 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 5e60fea1180cdea2dac00d067cafc332d054e396 to 31f7091498c64d6a44eff7702f5f55e3f769eaf2 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 22:02:31 to 01/21/2026 22:07:36 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## ef0c006cf - 2026-01-21 16:03:48 -0600 - 01/21/2026 16:03:47
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 1a45740107331f6e9aa14115277abc2e8e72d6cb to 5e60fea1180cdea2dac00d067cafc332d054e396 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:57:20 to 01/21/2026 22:02:31 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 1a45740107331f6e9aa14115277abc2e8e72d6cb to 5e60fea1180cdea2dac00d067cafc332d054e396 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:57:20 to 01/21/2026 22:02:31 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## a12151612 - 2026-01-21 15:59:15 -0600 - 01/21/2026 15:59:15
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from bb9ab32df6425cc4c3f7e85fe66b88fde559ad15 to 1a45740107331f6e9aa14115277abc2e8e72d6cb | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:50:11 to 01/21/2026 21:57:20 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from bb9ab32df6425cc4c3f7e85fe66b88fde559ad15 to 1a45740107331f6e9aa14115277abc2e8e72d6cb | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:50:11 to 01/21/2026 21:57:20 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## c23a1b2ba - 2026-01-21 15:52:32 -0600 - 01/21/2026 15:52:32
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from cc133b37285c49892eb75a0361ab1e1387102f4a to bb9ab32df6425cc4c3f7e85fe66b88fde559ad15 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:49:20 to 01/21/2026 21:50:11 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from cc133b37285c49892eb75a0361ab1e1387102f4a to bb9ab32df6425cc4c3f7e85fe66b88fde559ad15 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:49:20 to 01/21/2026 21:50:11 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## f8ca62eba - 2026-01-21 15:50:14 -0600 - 01/21/2026 15:50:14
Added in Other:
- DFFlagRbxStorageAvailableSpaceCreatePath_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:46:36 | Mechanism: Enables a new method for checking available storage space. | Purpose: Ensures players can save their creations without running into storage issues.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 90752e8aeee65744c5ad35eaed23a626c365b1ca to cc133b37285c49892eb75a0361ab1e1387102f4a | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:45:13 to 01/21/2026 21:49:20 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 90752e8aeee65744c5ad35eaed23a626c365b1ca to cc133b37285c49892eb75a0361ab1e1387102f4a | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:45:13 to 01/21/2026 21:49:20 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 4914296be - 2026-01-21 15:45:41 -0600 - 01/21/2026 15:45:41
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from aac2d6115b8e3b703c4acc59e73edaffb6908c6d to 90752e8aeee65744c5ad35eaed23a626c365b1ca | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:42:27 to 01/21/2026 21:45:13 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from aac2d6115b8e3b703c4acc59e73edaffb6908c6d to 90752e8aeee65744c5ad35eaed23a626c365b1ca | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:42:27 to 01/21/2026 21:45:13 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## dfd809adf - 2026-01-21 15:43:23 -0600 - 01/21/2026 15:43:22
Added in Camera/UI:
- FFlagUIBloxFixCoplayFooterConditionalHooks = True | Mechanism: Fixes issues with UI elements that depend on certain conditions in co-play settings. | Purpose: Improves the display and functionality of user interfaces when playing together with friends.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 32762cbefbe153de084846b4ac90d60b0deefbac to aac2d6115b8e3b703c4acc59e73edaffb6908c6d | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:36:38 to 01/21/2026 21:42:27 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 32762cbefbe153de084846b4ac90d60b0deefbac to aac2d6115b8e3b703c4acc59e73edaffb6908c6d | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:36:38 to 01/21/2026 21:42:27 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Camera/UI:
- FFlagUIBloxFixCoplayFooterConditionalHooks_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T20:36:56) | Mechanism: Fixes issues with conditional hooks in the UI framework for co-play features. | Purpose: Improves the user interface for players in co-play sessions, making it more reliable.

## 53b45efa5 - 2026-01-21 15:38:51 -0600 - 01/21/2026 15:38:50
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from abc0e8bcacbebc582e3219186e22a4cc14734b45 to 32762cbefbe153de084846b4ac90d60b0deefbac | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:35:55 to 01/21/2026 21:36:38 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from abc0e8bcacbebc582e3219186e22a4cc14734b45 to 32762cbefbe153de084846b4ac90d60b0deefbac | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:35:55 to 01/21/2026 21:36:38 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagAXScrollingListAutomaticCanvasSize_Staged removed (was true;SteadyState;10;30;Revert;2026-01-21T21:02:56) | Mechanism: Automatically adjusts the canvas size of scrolling lists. | Purpose: Enhances user experience by ensuring all items are visible without manual adjustments.

## 4a52d9364 - 2026-01-21 15:36:31 -0600 - 01/21/2026 15:36:31
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from c2a023751525f464983db21f0f9adada51d83975 to abc0e8bcacbebc582e3219186e22a4cc14734b45 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:32:57 to 01/21/2026 21:35:55 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from c2a023751525f464983db21f0f9adada51d83975 to abc0e8bcacbebc582e3219186e22a4cc14734b45 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:32:57 to 01/21/2026 21:35:55 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 1996c6303 - 2026-01-21 15:34:14 -0600 - 01/21/2026 15:34:13
Added in Other:
- DFFlagDirectMipCalc_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:32:06 | Mechanism: Enables direct calculation of mipmaps for textures. | Purpose: Improves texture quality and loading times in games.
Added in Graphics:
- FFlagFixFalseMipTextureFree_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:31:28 | Mechanism: Corrects issues with texture quality at different distances. | Purpose: Improves visual clarity and reduces blurriness in textures for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 3c05c547f3cb1d5aa2e83347a9ec611ba98e0df6 to c2a023751525f464983db21f0f9adada51d83975 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:29:56 to 01/21/2026 21:32:57 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 3c05c547f3cb1d5aa2e83347a9ec611ba98e0df6 to c2a023751525f464983db21f0f9adada51d83975 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:29:56 to 01/21/2026 21:32:57 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 6f2ddc0b8 - 2026-01-21 15:31:55 -0600 - 01/21/2026 15:31:54
Added in Graphics:
- FFlagSharedResolutionTexture_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:29:15 | Mechanism: Allows textures to share resolution settings across different parts of the game. | Purpose: Enhances visual consistency and performance in graphics.
Added in Network:
- SFFlagIAS_InstancePointersHoldAcrossReplication3_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:28:00 | Mechanism: Maintains references to game objects during data updates. | Purpose: Ensures smoother gameplay and object interactions for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 38324140fd14a0ae04281d66f9b19bcff5f5a9cd to 3c05c547f3cb1d5aa2e83347a9ec611ba98e0df6 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:23:17 to 01/21/2026 21:29:56 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 38324140fd14a0ae04281d66f9b19bcff5f5a9cd to 3c05c547f3cb1d5aa2e83347a9ec611ba98e0df6 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:23:17 to 01/21/2026 21:29:56 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## f9362faaf - 2026-01-21 15:25:00 -0600 - 01/21/2026 15:25:00
Added in Other:
- DFFlagRM3ScreenshotEncoding_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:22:26 | Mechanism: Changes the way screenshots are encoded for better quality. | Purpose: Improves the quality of screenshots taken by players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from d731728a8e85b42d336d4240430ae07b72c9cd88 to 38324140fd14a0ae04281d66f9b19bcff5f5a9cd | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:21:29 to 01/21/2026 21:23:17 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from d731728a8e85b42d336d4240430ae07b72c9cd88 to 38324140fd14a0ae04281d66f9b19bcff5f5a9cd | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:21:29 to 01/21/2026 21:23:17 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## d2e676a88 - 2026-01-21 15:22:40 -0600 - 01/21/2026 15:22:40
Added in Other:
- FFlagLogRewardedVideoPlayerButtonActions = True | Mechanism: Tracks user interactions with buttons in rewarded video ads. | Purpose: Helps developers understand player engagement with ads, leading to better rewards and ad experiences.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from b6e7b33fc3aeda92256ce2095ceab2774b53757a to d731728a8e85b42d336d4240430ae07b72c9cd88 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:16:59 to 01/21/2026 21:21:29 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from b6e7b33fc3aeda92256ce2095ceab2774b53757a to d731728a8e85b42d336d4240430ae07b72c9cd88 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:16:59 to 01/21/2026 21:21:29 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagRM3ScreenshotEncoding_Staged removed (was false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:07:09) | Mechanism: Changes the way screenshots are encoded for better quality. | Purpose: Improves the quality of screenshots taken by players.
- FFlagLogRewardedVideoPlayerButtonActions_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T20:17:30) | Mechanism: Tracks actions taken on buttons in rewarded video ads. | Purpose: Improves ad performance and player experience by understanding how players interact with ads.
Removed in Network:
- SFFlagIAS_InstancePointersHoldAcrossReplication3_Staged removed (was true;SteadyState;10;30;Revert;2026-01-21T20:45:51) | Mechanism: Maintains references to game objects during data updates. | Purpose: Ensures smoother gameplay and object interactions for players.

## eda0beb5c - 2026-01-21 15:18:08 -0600 - 01/21/2026 15:18:07
Added in Other:
- FFlagExplorerOptimizedHasChildren = True | Mechanism: Optimizes the way the Explorer panel checks for child objects in a hierarchy. | Purpose: Improves performance and responsiveness when navigating complex game structures.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from e41df4de257ae477f4e8b4e76ec7ff0505978f97 to b6e7b33fc3aeda92256ce2095ceab2774b53757a | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:14:57 to 01/21/2026 21:16:59 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from e41df4de257ae477f4e8b4e76ec7ff0505978f97 to b6e7b33fc3aeda92256ce2095ceab2774b53757a | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:14:57 to 01/21/2026 21:16:59 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagExplorerOptimizedHasChildren_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T20:12:57) | Mechanism: Optimizes the check for whether an object has children in the Explorer. | Purpose: Makes the Explorer faster and more responsive for users managing their game objects.

## 3dd316d65 - 2026-01-21 15:15:49 -0600 - 01/21/2026 15:15:49
Added in Other:
- DFFlagMoveEverythingA_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:13:03 | Mechanism: Allows movement of all game elements in a single operation. | Purpose: Simplifies the process of adjusting game layouts for developers.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 901307ffcc0e08f8e4e80075dbba6e3d46ea28e4 to e41df4de257ae477f4e8b4e76ec7ff0505978f97 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:12:39 to 01/21/2026 21:14:57 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 901307ffcc0e08f8e4e80075dbba6e3d46ea28e4 to e41df4de257ae477f4e8b4e76ec7ff0505978f97 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:12:39 to 01/21/2026 21:14:57 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## ce8a6abaf - 2026-01-21 15:13:32 -0600 - 01/21/2026 15:13:31
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from f8007fbaa09958c98f744102a25400f72142cbd7 to 901307ffcc0e08f8e4e80075dbba6e3d46ea28e4 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:07:50 to 01/21/2026 21:12:39 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from f8007fbaa09958c98f744102a25400f72142cbd7 to 901307ffcc0e08f8e4e80075dbba6e3d46ea28e4 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:07:50 to 01/21/2026 21:12:39 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## c0098da68 - 2026-01-21 15:08:57 -0600 - 01/21/2026 15:08:56
Added in Other:
- DFFlagRM3ScreenshotEncoding_Staged = false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T21:07:09 | Mechanism: Changes the way screenshots are encoded for better quality. | Purpose: Improves the quality of screenshots taken by players.
- FFlagVideoEnableHevcEncode2 = True | Mechanism: Activates a more efficient video encoding format for Roblox videos. | Purpose: Provides higher quality video streaming with less data usage for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from bdf99dafac5c5c782ae10d14fb13df05a9247d75 to f8007fbaa09958c98f744102a25400f72142cbd7 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:03:51 to 01/21/2026 21:07:50 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from bdf99dafac5c5c782ae10d14fb13df05a9247d75 to f8007fbaa09958c98f744102a25400f72142cbd7 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:03:51 to 01/21/2026 21:07:50 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagVideoEnableHevcEncode2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T20:04:39) | Mechanism: Enables a more efficient video encoding format (HEVC) for video uploads. | Purpose: Improves video quality and reduces file size for players uploading videos.

## d6c2bb923 - 2026-01-21 15:06:39 -0600 - 01/21/2026 15:06:38
Added in Other:
- FFlagAXScrollingListAutomaticCanvasSize_Staged = true;SteadyState;10;30;Revert;2026-01-21T21:02:56 | Mechanism: Automatically adjusts the canvas size of scrolling lists. | Purpose: Enhances user experience by ensuring all items are visible without manual adjustments.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 0b7b92c3fd2c4bfc3561143b4cfdd20b30a27078 to bdf99dafac5c5c782ae10d14fb13df05a9247d75 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:01:54 to 01/21/2026 21:03:51 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 0b7b92c3fd2c4bfc3561143b4cfdd20b30a27078 to bdf99dafac5c5c782ae10d14fb13df05a9247d75 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:01:54 to 01/21/2026 21:03:51 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## f12c8e212 - 2026-01-21 15:04:21 -0600 - 01/21/2026 15:04:21
Added in Camera/UI:
- FFlagAXCatalogCategoriesSDUILinks = True | Mechanism: Enables links in the catalog for categories in the new UI. | Purpose: Enhances user experience by making it easier for players to navigate and find items in the catalog.
- FFlagAXCatalogCategoriesSDUITaxonomy = True | Mechanism: Updates the categorization system for the asset catalog. | Purpose: Makes it easier for players to find and browse assets.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 450679fcf049b6fc257d41094f5cb950240b682f to 0b7b92c3fd2c4bfc3561143b4cfdd20b30a27078 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 21:00:43 to 01/21/2026 21:01:54 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 450679fcf049b6fc257d41094f5cb950240b682f to 0b7b92c3fd2c4bfc3561143b4cfdd20b30a27078 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 21:00:43 to 01/21/2026 21:01:54 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Camera/UI:
- FFlagAXCatalogCategoriesSDUILinks_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T19:59:04) | Mechanism: Introduces links in the catalog categories for easier navigation. | Purpose: Enhances user experience by allowing players to quickly access related items in the catalog.
- FFlagAXCatalogCategoriesSDUITaxonomy_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T20:00:27) | Mechanism: Implements a new categorization system for assets in the catalog. | Purpose: Makes it easier for players to find and browse through assets in the catalog.

## 8bd9cf64f - 2026-01-21 15:02:04 -0600 - 01/21/2026 15:02:04
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from fa0d3fb55299a6c58c2fae58bdc036bbb5fac017 to 450679fcf049b6fc257d41094f5cb950240b682f | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:53:11 to 01/21/2026 21:00:43 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from fa0d3fb55299a6c58c2fae58bdc036bbb5fac017 to 450679fcf049b6fc257d41094f5cb950240b682f | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:53:11 to 01/21/2026 21:00:43 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 9ad39011e - 2026-01-21 14:55:20 -0600 - 01/21/2026 14:55:20
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from b2e885bc1e7886299ea3f8fdc811f871cfc53a54 to fa0d3fb55299a6c58c2fae58bdc036bbb5fac017 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:51:23 to 01/21/2026 20:53:11 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from b2e885bc1e7886299ea3f8fdc811f871cfc53a54 to fa0d3fb55299a6c58c2fae58bdc036bbb5fac017 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:51:23 to 01/21/2026 20:53:11 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## c49dedb52 - 2026-01-21 14:53:00 -0600 - 01/21/2026 14:52:59
Added in Other:
- FFlagDevConsoleDownArrowIconFix = True | Mechanism: Fixes the icon display for the down arrow in the developer console. | Purpose: Improves the visual clarity of the developer console for better usability.
- FFlagExplorerHeartbeatTelemetry = True | Mechanism: Tracks and reports the activity of the Explorer tool in real-time. | Purpose: Helps developers understand how players use the Explorer, leading to better tools.
Added in Network:
- SFFlagIAS_InstancePointersHoldAcrossReplication3_Staged = true;SteadyState;10;30;Revert;2026-01-21T20:45:51 | Mechanism: Maintains references to game objects during data updates. | Purpose: Ensures smoother gameplay and object interactions for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from daa1d23702142d404000396bcf617f09b79dd2d4 to b2e885bc1e7886299ea3f8fdc811f871cfc53a54 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:46:51 to 01/21/2026 20:51:23 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from daa1d23702142d404000396bcf617f09b79dd2d4 to b2e885bc1e7886299ea3f8fdc811f871cfc53a54 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:46:51 to 01/21/2026 20:51:23 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagDevConsoleDownArrowIconFix_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T19:48:10) | Mechanism: Fixes the down arrow icon in the developer console. | Purpose: Improves the visual clarity of the developer console for better usability.
- FFlagExplorerHeartbeatTelemetry_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T19:49:24) | Mechanism: Tracks the performance of the Explorer tool in real-time. | Purpose: Ensures the Explorer tool runs efficiently, improving the development experience for creators.

## f8de25296 - 2026-01-21 14:48:27 -0600 - 01/21/2026 14:48:27
Added in Other:
- FFlagGImageWebPBiEndianLoad = True | Mechanism: Enables loading of WebP images in a specific byte order. | Purpose: Improves image loading performance and compatibility for games using WebP format.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from cc08b0748478379ff55c5ebe6b1ed649b55f1deb to daa1d23702142d404000396bcf617f09b79dd2d4 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:39:23 to 01/21/2026 20:46:51 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from cc08b0748478379ff55c5ebe6b1ed649b55f1deb to daa1d23702142d404000396bcf617f09b79dd2d4 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:39:23 to 01/21/2026 20:46:51 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagGImageWebPBiEndianLoad_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T19:44:39) | Mechanism: Allows loading of WebP images in a bi-endian format. | Purpose: Improves image loading efficiency and quality in games.
- FFlagRbxTelemetryEnableHttpRetries3_Staged removed (was true;SteadyState;10;30;Revert;true;387806565;2026-01-21T20:12:35) | Mechanism: Enables retry attempts for HTTP requests in the telemetry system. | Purpose: Increases reliability of data transmission, ensuring better game performance tracking.
- FFlagTelemetryRetryOnConnectFail_Staged removed (was true;SteadyState;10;30;Revert;true;387806565;2026-01-21T20:12:35) | Mechanism: Enables automatic retries when a connection to the server fails. | Purpose: Improves player experience by reducing connection issues and allowing smoother gameplay.
- FFlagTelemetryRetryOnDnsResolve_Staged removed (was true;SteadyState;10;30;Revert;true;387806565;2026-01-21T20:12:35) | Mechanism: Adds a retry mechanism for DNS resolution in telemetry data collection. | Purpose: Ensures more reliable data collection, leading to improved game performance and stability for players.

## 9910228b4 - 2026-01-21 14:41:42 -0600 - 01/21/2026 14:41:42
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 9ef98c7f3eaf3b6d77c3aee402fa2d8ee26d84b6 to cc08b0748478379ff55c5ebe6b1ed649b55f1deb | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:37:36 to 01/21/2026 20:39:23 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 9ef98c7f3eaf3b6d77c3aee402fa2d8ee26d84b6 to cc08b0748478379ff55c5ebe6b1ed649b55f1deb | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:37:36 to 01/21/2026 20:39:23 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 34296b928 - 2026-01-21 14:39:24 -0600 - 01/21/2026 14:39:24
Added in Camera/UI:
- FFlagUIBloxFixCoplayFooterConditionalHooks_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T20:36:56 | Mechanism: Fixes issues with conditional hooks in the UI framework for co-play features. | Purpose: Improves the user interface for players in co-play sessions, making it more reliable.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from a14617adee757464cf654de1043f08281ecf00df to 9ef98c7f3eaf3b6d77c3aee402fa2d8ee26d84b6 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:26:39 to 01/21/2026 20:37:36 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from a14617adee757464cf654de1043f08281ecf00df to 9ef98c7f3eaf3b6d77c3aee402fa2d8ee26d84b6 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:26:39 to 01/21/2026 20:37:36 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 0a4398250 - 2026-01-21 14:28:08 -0600 - 01/21/2026 14:28:08
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from e6b92db3c0a09b4e01e5178d18a8dfe5457b63d8 to a14617adee757464cf654de1043f08281ecf00df | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:21:59 to 01/21/2026 20:26:39 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from e6b92db3c0a09b4e01e5178d18a8dfe5457b63d8 to a14617adee757464cf654de1043f08281ecf00df | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:21:59 to 01/21/2026 20:26:39 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 32c2925d6 - 2026-01-21 14:23:36 -0600 - 01/21/2026 14:23:35
Added in Other:
- FFlagAXHandleCategoryIdsTaxonomyDeepLinks = True | Mechanism: Enhances how category IDs are managed in deep links for navigation. | Purpose: Allows players to navigate directly to specific categories more easily.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from a9c35f35c602fd078e2d140fecc0275ff319afb7 to e6b92db3c0a09b4e01e5178d18a8dfe5457b63d8 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:18:37 to 01/21/2026 20:21:59 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from a9c35f35c602fd078e2d140fecc0275ff319afb7 to e6b92db3c0a09b4e01e5178d18a8dfe5457b63d8 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:18:37 to 01/21/2026 20:21:59 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagAXHandleCategoryIdsTaxonomyDeepLinks_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T19:19:47) | Mechanism: Implements deep linking for category IDs in the taxonomy system. | Purpose: Allows players to easily navigate to specific categories in the game store.

## 3bdca36ca - 2026-01-21 14:21:17 -0600 - 01/21/2026 14:21:17
Added in Other:
- FFlagLogRewardedVideoPlayerButtonActions_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T20:17:30 | Mechanism: Tracks actions taken on buttons in rewarded video ads. | Purpose: Improves ad performance and player experience by understanding how players interact with ads.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 09b0408f0a8c343b469d7572b7ceb9c3c1b15e49 to a9c35f35c602fd078e2d140fecc0275ff319afb7 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:16:39 to 01/21/2026 20:18:37 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 09b0408f0a8c343b469d7572b7ceb9c3c1b15e49 to a9c35f35c602fd078e2d140fecc0275ff319afb7 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:16:39 to 01/21/2026 20:18:37 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 3250c9c80 - 2026-01-21 14:19:02 -0600 - 01/21/2026 14:19:01
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 12d90f13dd212f30bd479e4722f2201703d99f34 to 09b0408f0a8c343b469d7572b7ceb9c3c1b15e49 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:15:44 to 01/21/2026 20:16:39 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 12d90f13dd212f30bd479e4722f2201703d99f34 to 09b0408f0a8c343b469d7572b7ceb9c3c1b15e49 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:15:44 to 01/21/2026 20:16:39 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## de393de46 - 2026-01-21 14:16:45 -0600 - 01/21/2026 14:16:45
Added in Other:
- FFlagExplorerOptimizedHasChildren_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T20:12:57 | Mechanism: Optimizes the check for whether an object has children in the Explorer. | Purpose: Makes the Explorer faster and more responsive for users managing their game objects.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 25fb87dd6a515dcb2e6c789fbf00672ea29b8e13 to 12d90f13dd212f30bd479e4722f2201703d99f34 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:13:45 to 01/21/2026 20:15:44 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 25fb87dd6a515dcb2e6c789fbf00672ea29b8e13 to 12d90f13dd212f30bd479e4722f2201703d99f34 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:13:45 to 01/21/2026 20:15:44 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 1ab70b8fc - 2026-01-21 14:14:28 -0600 - 01/21/2026 14:14:27
Added in Other:
- FFlagRbxTelemetryEnableHttpRetries3_Staged = true;SteadyState;10;30;Revert;true;387806565;2026-01-21T20:12:35 | Mechanism: Enables retry attempts for HTTP requests in the telemetry system. | Purpose: Increases reliability of data transmission, ensuring better game performance tracking.
- FFlagTelemetryRetryOnConnectFail_Staged = true;SteadyState;10;30;Revert;true;387806565;2026-01-21T20:12:35 | Mechanism: Enables automatic retries when a connection to the server fails. | Purpose: Improves player experience by reducing connection issues and allowing smoother gameplay.
- FFlagTelemetryRetryOnDnsResolve_Staged = true;SteadyState;10;30;Revert;true;387806565;2026-01-21T20:12:35 | Mechanism: Adds a retry mechanism for DNS resolution in telemetry data collection. | Purpose: Ensures more reliable data collection, leading to improved game performance and stability for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from f4e456e90dc749ecbb1a6b4fe08e51c335f212b2 to 25fb87dd6a515dcb2e6c789fbf00672ea29b8e13 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:07:03 to 01/21/2026 20:13:45 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from f4e456e90dc749ecbb1a6b4fe08e51c335f212b2 to 25fb87dd6a515dcb2e6c789fbf00672ea29b8e13 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:07:03 to 01/21/2026 20:13:45 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## a48dc5ce8 - 2026-01-21 14:09:58 -0600 - 01/21/2026 14:09:57
Added in Other:
- FFlagPerformanceControlBudgetSystemRollout10 = True | Mechanism: Implements a new system to manage performance budgets for games. | Purpose: Helps developers optimize their games for better performance, leading to smoother gameplay for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from c1ebc76569cdd3ca06fb074a154ba0ff78783b0c to f4e456e90dc749ecbb1a6b4fe08e51c335f212b2 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:05:39 to 01/21/2026 20:07:03 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from c1ebc76569cdd3ca06fb074a154ba0ff78783b0c to f4e456e90dc749ecbb1a6b4fe08e51c335f212b2 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:05:39 to 01/21/2026 20:07:03 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagPerformanceControlBudgetSystemRollout10_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:58:31) | Mechanism: Implements a new system to manage performance budgets for games. | Purpose: Ensures smoother gameplay by optimizing resource usage.

## 560b9e725 - 2026-01-21 14:07:43 -0600 - 01/21/2026 14:07:43
Added in Other:
- FFlagVideoEnableHevcEncode2_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T20:04:39 | Mechanism: Enables a more efficient video encoding format (HEVC) for video uploads. | Purpose: Improves video quality and reduces file size for players uploading videos.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from bbb1aec0bacfa2729cfcf8a2e434ec297afff547 to c1ebc76569cdd3ca06fb074a154ba0ff78783b0c | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 20:01:12 to 01/21/2026 20:05:39 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from bbb1aec0bacfa2729cfcf8a2e434ec297afff547 to c1ebc76569cdd3ca06fb074a154ba0ff78783b0c | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 20:01:12 to 01/21/2026 20:05:39 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 1e4165c94 - 2026-01-21 14:03:12 -0600 - 01/21/2026 14:03:11
Added in Camera/UI:
- FFlagAXCatalogCategoriesSDUITaxonomy_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T20:00:27 | Mechanism: Implements a new categorization system for assets in the catalog. | Purpose: Makes it easier for players to find and browse through assets in the catalog.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 6d958c3d9bedd893cbfc975f6b702ce946a9e004 to bbb1aec0bacfa2729cfcf8a2e434ec297afff547 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 19:59:58 to 01/21/2026 20:01:12 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 6d958c3d9bedd893cbfc975f6b702ce946a9e004 to bbb1aec0bacfa2729cfcf8a2e434ec297afff547 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 19:59:58 to 01/21/2026 20:01:12 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## af34c3280 - 2026-01-21 14:00:54 -0600 - 01/21/2026 14:00:53
Added in Camera/UI:
- FFlagAXCatalogCategoriesSDUILinks_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T19:59:04 | Mechanism: Introduces links in the catalog categories for easier navigation. | Purpose: Enhances user experience by allowing players to quickly access related items in the catalog.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from ab78fe8e4d722b6661bd4229ae1d08c2417ef544 to 6d958c3d9bedd893cbfc975f6b702ce946a9e004 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 19:57:04 to 01/21/2026 19:59:58 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from ab78fe8e4d722b6661bd4229ae1d08c2417ef544 to 6d958c3d9bedd893cbfc975f6b702ce946a9e004 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 19:57:04 to 01/21/2026 19:59:58 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## c5d94883f - 2026-01-21 13:58:37 -0600 - 01/21/2026 13:58:36
Added in Other:
- FFlagAndroidHevcEncoderCheck = True | Mechanism: Checks for support of HEVC encoding on Android devices. | Purpose: Ensures better video quality and compression for players using compatible Android devices.
- FFlagEnablePackagePublishFailureMetrics = True | Mechanism: Tracks and reports errors when publishing packages fails. | Purpose: Helps developers understand and fix issues when their packages don't publish correctly.
- FFlagSQLiteCacheFixContains = True | Mechanism: Fixes how the SQLite cache checks for existing entries. | Purpose: Improves data retrieval speed, leading to smoother gameplay.
- FFlagSQLiteCacheFixName = True | Mechanism: Corrects the naming issues in the SQLite caching system. | Purpose: Improves data retrieval speed and reliability for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 1caa745e5184f77d81912d83763a517ef36fa461 to ab78fe8e4d722b6661bd4229ae1d08c2417ef544 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 19:50:17 to 01/21/2026 19:57:04 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 1caa745e5184f77d81912d83763a517ef36fa461 to ab78fe8e4d722b6661bd4229ae1d08c2417ef544 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 19:50:17 to 01/21/2026 19:57:04 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagAndroidHevcEncoderCheck_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:49:46) | Mechanism: Enables a check for using a more efficient video encoding format on Android devices. | Purpose: Enhances video quality and reduces file size for smoother gameplay on mobile devices.
- FFlagEnablePackagePublishFailureMetrics_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:53:14) | Mechanism: Tracks and reports failures when publishing packages. | Purpose: Helps developers understand and fix issues when sharing their creations.
- FFlagSQLiteCacheFixContains_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:55:13) | Mechanism: Fixes issues with the SQLite cache to ensure accurate data retrieval. | Purpose: Improves game performance and reliability by ensuring players see the correct information.
- FFlagSQLiteCacheFixName_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:54:43) | Mechanism: Addresses issues with naming in the SQLite cache system. | Purpose: Ensures better organization and access to game data for developers.

## b770bfbde - 2026-01-21 13:51:49 -0600 - 01/21/2026 13:51:49
Added in Other:
- FFlagDevConsoleDownArrowIconFix_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T19:48:10 | Mechanism: Fixes the down arrow icon in the developer console. | Purpose: Improves the visual clarity of the developer console for better usability.
- FFlagExplorerHeartbeatTelemetry_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T19:49:24 | Mechanism: Tracks the performance of the Explorer tool in real-time. | Purpose: Ensures the Explorer tool runs efficiently, improving the development experience for creators.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from fa4a761c6c4e4257e25d846094082d965a03fac9 to 1caa745e5184f77d81912d83763a517ef36fa461 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 19:46:54 to 01/21/2026 19:50:17 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from fa4a761c6c4e4257e25d846094082d965a03fac9 to 1caa745e5184f77d81912d83763a517ef36fa461 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 19:46:54 to 01/21/2026 19:50:17 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## fb49c0f3d - 2026-01-21 13:49:31 -0600 - 01/21/2026 13:49:30
Added in Network:
- FFlagAudioDeviceInputFixReplicationChecks = True | Mechanism: Fixes how audio input devices are checked and replicated in games. | Purpose: Ensures better audio quality and functionality for players using different audio devices.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 45f3432bb752326ba163530b20af8eeb079ab5c1 to fa4a761c6c4e4257e25d846094082d965a03fac9 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 19:46:33 to 01/21/2026 19:46:54 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 45f3432bb752326ba163530b20af8eeb079ab5c1 to fa4a761c6c4e4257e25d846094082d965a03fac9 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 19:46:33 to 01/21/2026 19:46:54 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Network:
- FFlagAudioDeviceInputFixReplicationChecks_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:44:20) | Mechanism: Fixes issues with how audio device inputs are checked and replicated across devices. | Purpose: Ensures consistent audio experiences for players, improving sound quality and functionality.

## 8664aec0f - 2026-01-21 13:47:14 -0600 - 01/21/2026 13:47:14
Added in Other:
- FFlagGImageWebPBiEndianLoad_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T19:44:39 | Mechanism: Allows loading of WebP images in a bi-endian format. | Purpose: Improves image loading efficiency and quality in games.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from a19cd15e7116a3ab7ec5f0756a85b0f714fe47f5 to 45f3432bb752326ba163530b20af8eeb079ab5c1 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 19:36:39 to 01/21/2026 19:46:33 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from a19cd15e7116a3ab7ec5f0756a85b0f714fe47f5 to 45f3432bb752326ba163530b20af8eeb079ab5c1 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 19:36:39 to 01/21/2026 19:46:33 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## a5d7feab3 - 2026-01-21 13:38:21 -0600 - 01/21/2026 13:38:21
Changed in Other:
- DFIntSimAdaptiveExtraIterations changed from 4 to 6 | Mechanism: Adjusts the number of iterations in simulations based on performance. | Purpose: Optimizes game performance, leading to a smoother experience for players during complex simulations.
- DFStringFlagRepoGitHashDynamicString changed from 2427952aa6db399364d108a7182756095478b7d6 to a19cd15e7116a3ab7ec5f0756a85b0f714fe47f5 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 19:27:17 to 01/21/2026 19:36:39 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 2427952aa6db399364d108a7182756095478b7d6 to a19cd15e7116a3ab7ec5f0756a85b0f714fe47f5 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 19:27:17 to 01/21/2026 19:36:39 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFIntSimAdaptiveExtraIterations_Staged removed (was 6;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:30:46) | Mechanism: Increases the number of iterations in simulations for better accuracy. | Purpose: Enhances game performance and realism, leading to smoother gameplay for players.

## 7f0e57dae - 2026-01-21 13:29:26 -0600 - 01/21/2026 13:29:26
Added in Other:
- FFlagAsyncLoadRvSubsystem = True | Mechanism: Enables asynchronous loading for the rendering subsystem. | Purpose: Improves loading times and performance, leading to a smoother gaming experience.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 1857239de133466bf4a4096616c9f19a6cc0914d to 2427952aa6db399364d108a7182756095478b7d6 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 19:23:38 to 01/21/2026 19:27:17 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 1857239de133466bf4a4096616c9f19a6cc0914d to 2427952aa6db399364d108a7182756095478b7d6 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 19:23:38 to 01/21/2026 19:27:17 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagAsyncLoadRvSubsystem_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:24:00) | Mechanism: Loads certain game elements asynchronously to reduce loading times. | Purpose: Enhances the overall game experience by making it faster and smoother.

## eddaa34f2 - 2026-01-21 13:24:46 -0600 - 01/21/2026 13:24:45
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from cc7a70df98f091a927b298b3ffe0870778e5d114 to 1857239de133466bf4a4096616c9f19a6cc0914d | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 19:21:48 to 01/21/2026 19:23:38 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from cc7a70df98f091a927b298b3ffe0870778e5d114 to 1857239de133466bf4a4096616c9f19a6cc0914d | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 19:21:48 to 01/21/2026 19:23:38 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 8b6096fae - 2026-01-21 13:22:28 -0600 - 01/21/2026 13:22:27
Added in Other:
- FFlagAXFixHydratedWidgetsParams2 = True | Mechanism: Fixes issues with parameters for hydrated widgets in the user interface. | Purpose: Ensures a more stable and responsive UI experience for players.
- FFlagAXHandleCategoryIdsTaxonomyDeepLinks_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T19:19:47 | Mechanism: Implements deep linking for category IDs in the taxonomy system. | Purpose: Allows players to easily navigate to specific categories in the game store.
- FIntCoreScriptsProfilerSamplingHundredthsPercent = 1000 | Mechanism: Adjusts the sampling rate for profiling core scripts to a finer percentage. | Purpose: Improves the accuracy of performance tracking, helping developers create better experiences for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from f078a89788194daa9afc916b58666cade10e7608 to cc7a70df98f091a927b298b3ffe0870778e5d114 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 19:17:21 to 01/21/2026 19:21:48 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from f078a89788194daa9afc916b58666cade10e7608 to cc7a70df98f091a927b298b3ffe0870778e5d114 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 19:17:21 to 01/21/2026 19:21:48 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagAXFixHydratedWidgetsParams2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:18:55) | Mechanism: Fixes issues with how widget parameters are processed in the system. | Purpose: Improves the performance and reliability of widgets for a smoother user experience.
- FIntCoreScriptsProfilerSamplingHundredthsPercent_Staged removed (was 1000;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:17:45) | Mechanism: Improves performance tracking by sampling at a finer resolution. | Purpose: Enhances game stability and performance for a better gaming experience.

## 3f1b31db7 - 2026-01-21 13:20:10 -0600 - 01/21/2026 13:20:10
Added in Other:
- DFFlagRM3ScreenshotEncoding = True | Mechanism: Changes how screenshots are encoded for better quality. | Purpose: Provides players with higher quality screenshots of their gameplay.
- FFlagACSUGCValidationRCCOnly = True | Mechanism: Restricts user-generated content validation to a specific set of rules. | Purpose: Ensures that only approved content types are validated, improving safety and quality.
- FFlagStylingCachedPropertiesConst = True | Mechanism: Caches styling properties for faster access during rendering. | Purpose: Improves game loading times and visual performance for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from fafd11a4ac363503a1ffe304f3c74e4066edd928 to f078a89788194daa9afc916b58666cade10e7608 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 19:15:11 to 01/21/2026 19:17:21 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from fafd11a4ac363503a1ffe304f3c74e4066edd928 to f078a89788194daa9afc916b58666cade10e7608 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 19:15:11 to 01/21/2026 19:17:21 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagRM3ScreenshotEncoding_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:07:33) | Mechanism: Changes the way screenshots are encoded for better quality. | Purpose: Improves the quality of screenshots taken by players.
- FFlagACSUGCValidationRCCOnly_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:09:21) | Mechanism: Restricts user-generated content validation to a specific method. | Purpose: Ensures better quality control for user-generated content, leading to a safer and more enjoyable experience.
- FFlagStylingCachedPropertiesConst_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:14:13) | Mechanism: Caches styling properties to speed up rendering and reduce load times. | Purpose: Provides a faster and more responsive user interface for players.

## eebd2ecf8 - 2026-01-21 13:17:53 -0600 - 01/21/2026 13:17:53
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 1702448c135fd17f87ff607112cc9ebbe71262fd to fafd11a4ac363503a1ffe304f3c74e4066edd928 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 19:01:59 to 01/21/2026 19:15:11 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 1702448c135fd17f87ff607112cc9ebbe71262fd to fafd11a4ac363503a1ffe304f3c74e4066edd928 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 19:01:59 to 01/21/2026 19:15:11 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 61a48c0d9 - 2026-01-21 13:04:27 -0600 - 01/21/2026 13:04:26
Added in Other:
- FFlagAddDisableHangReportingOnDebuggerBreak2 = True | Mechanism: Adds an option to disable reporting when the debugger is paused. | Purpose: Reduces interruptions for developers, allowing them to focus on fixing issues without distractions.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 425396dc5eb690b0153fa63cd957b122cb02f544 to 1702448c135fd17f87ff607112cc9ebbe71262fd | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 18:59:22 to 01/21/2026 19:01:59 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 425396dc5eb690b0153fa63cd957b122cb02f544 to 1702448c135fd17f87ff607112cc9ebbe71262fd | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 18:59:22 to 01/21/2026 19:01:59 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagAddDisableHangReportingOnDebuggerBreak2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T17:57:41) | Mechanism: Allows developers to disable reporting when the debugger is paused. | Purpose: Reduces unnecessary interruptions during debugging, making it smoother for developers.

## 187decc55 - 2026-01-21 13:02:08 -0600 - 01/21/2026 13:02:08
Added in Other:
- FFlagPerformanceControlBudgetSystemRollout10_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:58:31 | Mechanism: Implements a new system to manage performance budgets for games. | Purpose: Ensures smoother gameplay by optimizing resource usage.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from d90a19fd523b0680014657217d26268d2f92a1df to 425396dc5eb690b0153fa63cd957b122cb02f544 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 18:56:58 to 01/21/2026 18:59:22 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from d90a19fd523b0680014657217d26268d2f92a1df to 425396dc5eb690b0153fa63cd957b122cb02f544 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 18:56:58 to 01/21/2026 18:59:22 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## fac4e58c0 - 2026-01-21 12:57:34 -0600 - 01/21/2026 12:57:34
Added in Other:
- FFlagSQLiteCacheFixContains_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:55:13 | Mechanism: Fixes issues with the SQLite cache to ensure accurate data retrieval. | Purpose: Improves game performance and reliability by ensuring players see the correct information.
- FFlagSQLiteCacheFixName_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:54:43 | Mechanism: Addresses issues with naming in the SQLite cache system. | Purpose: Ensures better organization and access to game data for developers.
- FFlagSupportTerminalMilestoneInReactProfilerLogger = True | Mechanism: Adds support for tracking performance milestones in a logging tool. | Purpose: Helps developers optimize game performance, leading to smoother gameplay for players.
- FFlagTelemetryCacheTrackBytes = True | Mechanism: Tracks the amount of data used for telemetry caching. | Purpose: Players benefit from better performance and stability in the game due to optimized data handling.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from e944c19dc8e28f6c979a766754ad4a008a433008 to d90a19fd523b0680014657217d26268d2f92a1df | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 18:54:11 to 01/21/2026 18:56:58 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from e944c19dc8e28f6c979a766754ad4a008a433008 to d90a19fd523b0680014657217d26268d2f92a1df | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 18:54:11 to 01/21/2026 18:56:58 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagSupportTerminalMilestoneInReactProfilerLogger_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T17:50:54) | Mechanism: Integrates terminal milestone tracking into the React profiler for performance analysis. | Purpose: Helps developers optimize game performance by providing better insights into application behavior.
- FFlagTelemetryCacheTrackBytes_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T17:50:57) | Mechanism: Tracks the amount of data used in telemetry more accurately. | Purpose: Helps developers understand data usage better, leading to improved game performance.

## 32570e96b - 2026-01-21 12:55:17 -0600 - 01/21/2026 12:55:17
Added in Other:
- FFlagAddVideoDetectorWrapper = True | Mechanism: Introduces a new system to detect video playback. | Purpose: Enhances video experience and ensures smoother playback for users.
- FFlagEnablePackagePublishFailureMetrics_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:53:14 | Mechanism: Tracks and reports failures when publishing packages. | Purpose: Helps developers understand and fix issues when sharing their creations.
Added in Camera/UI:
- FFlagRemoveExperienceMenuABTestManager = True | Mechanism: Discontinues the A/B testing for the experience menu. | Purpose: Provides a consistent experience menu for all players without variations.
- FFlagSduiBadgeTileContained = True | Mechanism: Modifies how badge tiles are displayed in the user interface. | Purpose: Enhances the visual presentation of badges, making them more appealing to players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 572d649795d0ff8e9ce79cbaf76853c04a844ee2 to e944c19dc8e28f6c979a766754ad4a008a433008 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 18:51:02 to 01/21/2026 18:54:11 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 572d649795d0ff8e9ce79cbaf76853c04a844ee2 to e944c19dc8e28f6c979a766754ad4a008a433008 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 18:51:02 to 01/21/2026 18:54:11 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagAddVideoDetectorWrapper_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T17:47:06) | Mechanism: Integrates a wrapper for detecting video content. | Purpose: Enhances the ability to manage and display video content in games.
Removed in Camera/UI:
- FFlagRemoveExperienceMenuABTestManager_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;70130128;2026-01-21T17:46:08) | Mechanism: Removes the A/B testing manager for the experience menu. | Purpose: Simplifies the experience menu for players by removing unnecessary testing features.
- FFlagSduiBadgeTileContained_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;308554894;2026-01-21T17:47:00) | Mechanism: Modifies how badge tiles are displayed in the user interface. | Purpose: Players can see their badges more clearly and access them more conveniently.

## 7a2a7066d - 2026-01-21 12:52:58 -0600 - 01/21/2026 12:52:58
Added in Other:
- FFlagAndroidHevcEncoderCheck_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:49:46 | Mechanism: Enables a check for using a more efficient video encoding format on Android devices. | Purpose: Enhances video quality and reduces file size for smoother gameplay on mobile devices.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 0a65b76f2360c10d4a22797dfc3ab74be3c7a548 to 572d649795d0ff8e9ce79cbaf76853c04a844ee2 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 18:47:06 to 01/21/2026 18:51:02 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 0a65b76f2360c10d4a22797dfc3ab74be3c7a548 to 572d649795d0ff8e9ce79cbaf76853c04a844ee2 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 18:47:06 to 01/21/2026 18:51:02 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 772b9d18a - 2026-01-21 12:48:30 -0600 - 01/21/2026 12:48:29
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 7b6ada8b4abf513a0b48f40e2a3878f23494f5df to 0a65b76f2360c10d4a22797dfc3ab74be3c7a548 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 18:45:37 to 01/21/2026 18:47:06 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 7b6ada8b4abf513a0b48f40e2a3878f23494f5df to 0a65b76f2360c10d4a22797dfc3ab74be3c7a548 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 18:45:37 to 01/21/2026 18:47:06 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 72ae302e9 - 2026-01-21 12:46:13 -0600 - 01/21/2026 12:46:13
Added in Network:
- FFlagAudioDeviceInputFixReplicationChecks_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:44:20 | Mechanism: Fixes issues with how audio device inputs are checked and replicated across devices. | Purpose: Ensures consistent audio experiences for players, improving sound quality and functionality.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 26868224b25e4f7e319a2305aea352f3cea5eb96 to 7b6ada8b4abf513a0b48f40e2a3878f23494f5df | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 18:42:05 to 01/21/2026 18:45:37 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 26868224b25e4f7e319a2305aea352f3cea5eb96 to 7b6ada8b4abf513a0b48f40e2a3878f23494f5df | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 18:42:05 to 01/21/2026 18:45:37 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 10711fd53 - 2026-01-21 12:43:56 -0600 - 01/21/2026 12:43:55
Added in Other:
- FFlagFastVideoFrameSamplerSeek = True | Mechanism: Improves the speed of seeking to different frames in video playback. | Purpose: Provides a smoother video experience for players by reducing lag when jumping to different parts of a video.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from dbe329ba0476ea8bb726aff3f4d353fe2f8be93c to 26868224b25e4f7e319a2305aea352f3cea5eb96 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 18:36:59 to 01/21/2026 18:42:05 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from dbe329ba0476ea8bb726aff3f4d353fe2f8be93c to 26868224b25e4f7e319a2305aea352f3cea5eb96 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 18:36:59 to 01/21/2026 18:42:05 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagFastVideoFrameSamplerSeek_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T17:38:20) | Mechanism: Enhances the speed at which video frames are sampled during playback. | Purpose: Provides a smoother video playback experience for players.

## a15c753a0 - 2026-01-21 12:39:26 -0600 - 01/21/2026 12:39:26
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 57bc0fff671cf47e1f35931f0433715248d3f5a7 to dbe329ba0476ea8bb726aff3f4d353fe2f8be93c | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 18:36:03 to 01/21/2026 18:36:59 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 57bc0fff671cf47e1f35931f0433715248d3f5a7 to dbe329ba0476ea8bb726aff3f4d353fe2f8be93c | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 18:36:03 to 01/21/2026 18:36:59 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## c51bb3aa5 - 2026-01-21 12:37:11 -0600 - 01/21/2026 12:37:10
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 0e843b2584aeb05719173948f5e40b367a6c3c8f to 57bc0fff671cf47e1f35931f0433715248d3f5a7 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 18:31:32 to 01/21/2026 18:36:03 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 0e843b2584aeb05719173948f5e40b367a6c3c8f to 57bc0fff671cf47e1f35931f0433715248d3f5a7 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 18:31:32 to 01/21/2026 18:36:03 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 231c3f3ca - 2026-01-21 12:32:42 -0600 - 01/21/2026 12:32:42
Added in Other:
- DFIntSimAdaptiveExtraIterations_Staged = 6;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:30:46 | Mechanism: Increases the number of iterations in simulations for better accuracy. | Purpose: Enhances game performance and realism, leading to smoother gameplay for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 77a17449061c7bc33749c5aa30864eedc02e7d65 to 0e843b2584aeb05719173948f5e40b367a6c3c8f | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 18:25:17 to 01/21/2026 18:31:32 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 77a17449061c7bc33749c5aa30864eedc02e7d65 to 0e843b2584aeb05719173948f5e40b367a6c3c8f | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 18:25:17 to 01/21/2026 18:31:32 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 3e61182e5 - 2026-01-21 12:26:02 -0600 - 01/21/2026 12:26:02
Added in Other:
- FFlagAsyncLoadRvSubsystem_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:24:00 | Mechanism: Loads certain game elements asynchronously to reduce loading times. | Purpose: Enhances the overall game experience by making it faster and smoother.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from a031a53c4edb8aafdac93f51455ad8af0c4fcfd7 to 77a17449061c7bc33749c5aa30864eedc02e7d65 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 18:22:22 to 01/21/2026 18:25:17 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from a031a53c4edb8aafdac93f51455ad8af0c4fcfd7 to 77a17449061c7bc33749c5aa30864eedc02e7d65 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 18:22:22 to 01/21/2026 18:25:17 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## fe11db349 - 2026-01-21 12:23:45 -0600 - 01/21/2026 12:23:45
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from b8bb47580afeaa469e3bf3b8d0d5ed12e087bb7f to a031a53c4edb8aafdac93f51455ad8af0c4fcfd7 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 18:19:54 to 01/21/2026 18:22:22 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from b8bb47580afeaa469e3bf3b8d0d5ed12e087bb7f to a031a53c4edb8aafdac93f51455ad8af0c4fcfd7 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 18:19:54 to 01/21/2026 18:22:22 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 3641004e2 - 2026-01-21 12:21:28 -0600 - 01/21/2026 12:21:28
Added in Other:
- FFlagAXFixHydratedWidgetsParams2_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:18:55 | Mechanism: Fixes issues with how widget parameters are processed in the system. | Purpose: Improves the performance and reliability of widgets for a smoother user experience.
- FIntCoreScriptsProfilerSamplingHundredthsPercent_Staged = 1000;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:17:45 | Mechanism: Improves performance tracking by sampling at a finer resolution. | Purpose: Enhances game stability and performance for a better gaming experience.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 64d92c28dcea1491aa6357a31de0c28f42cc166b to b8bb47580afeaa469e3bf3b8d0d5ed12e087bb7f | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 18:17:40 to 01/21/2026 18:19:54 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 64d92c28dcea1491aa6357a31de0c28f42cc166b to b8bb47580afeaa469e3bf3b8d0d5ed12e087bb7f | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 18:17:40 to 01/21/2026 18:19:54 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## b2148da83 - 2026-01-21 12:19:12 -0600 - 01/21/2026 12:19:12
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 98d662814f6264facc9272571cddaefa4376ef55 to 64d92c28dcea1491aa6357a31de0c28f42cc166b | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 18:15:28 to 01/21/2026 18:17:40 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 98d662814f6264facc9272571cddaefa4376ef55 to 64d92c28dcea1491aa6357a31de0c28f42cc166b | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 18:15:28 to 01/21/2026 18:17:40 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## b7641e2e9 - 2026-01-21 12:16:54 -0600 - 01/21/2026 12:16:54
Added in Other:
- FFlagStylingCachedPropertiesConst_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:14:13 | Mechanism: Caches styling properties to speed up rendering and reduce load times. | Purpose: Provides a faster and more responsive user interface for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 8033162599cade0d0aa10b5740f4a81e56e3fe0b to 98d662814f6264facc9272571cddaefa4376ef55 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 18:10:19 to 01/21/2026 18:15:28 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 8033162599cade0d0aa10b5740f4a81e56e3fe0b to 98d662814f6264facc9272571cddaefa4376ef55 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 18:10:19 to 01/21/2026 18:15:28 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## c6eceb8c8 - 2026-01-21 12:12:25 -0600 - 01/21/2026 12:12:25
Added in Other:
- DFIntRobloxTelemetryBatchedReporterTimerIntervalMs_IXP = 1;Engine.Telemetry;engine_telemetry_v2_30_second_sending_interval;2067951443;flagbank | Mechanism: Sets the interval for batching telemetry reports in milliseconds. | Purpose: Optimizes performance by reducing the frequency of telemetry data sent, improving game efficiency.
- FFlagACSUGCValidationRCCOnly_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:09:21 | Mechanism: Restricts user-generated content validation to a specific method. | Purpose: Ensures better quality control for user-generated content, leading to a safer and more enjoyable experience.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 8bd5b72efd32f95426477226b9a9ce3e01eb1447 to 8033162599cade0d0aa10b5740f4a81e56e3fe0b | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 18:08:33 to 01/21/2026 18:10:19 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 8bd5b72efd32f95426477226b9a9ce3e01eb1447 to 8033162599cade0d0aa10b5740f4a81e56e3fe0b | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 18:08:33 to 01/21/2026 18:10:19 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## f846ba8c7 - 2026-01-21 12:10:10 -0600 - 01/21/2026 12:10:10
Added in Other:
- DFFlagRM3ScreenshotEncoding_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T18:07:33 | Mechanism: Changes the way screenshots are encoded for better quality. | Purpose: Improves the quality of screenshots taken by players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from f3bd26b70c7d7f8ffe00b16dc2ef2b5a737fb089 to 8bd5b72efd32f95426477226b9a9ce3e01eb1447 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 18:06:50 to 01/21/2026 18:08:33 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from f3bd26b70c7d7f8ffe00b16dc2ef2b5a737fb089 to 8bd5b72efd32f95426477226b9a9ce3e01eb1447 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 18:06:50 to 01/21/2026 18:08:33 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 829eec67f - 2026-01-21 12:07:53 -0600 - 01/21/2026 12:07:53
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from a06256709be781419b87b94936884796be68846b to f3bd26b70c7d7f8ffe00b16dc2ef2b5a737fb089 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 18:04:51 to 01/21/2026 18:06:50 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from a06256709be781419b87b94936884796be68846b to f3bd26b70c7d7f8ffe00b16dc2ef2b5a737fb089 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 18:04:51 to 01/21/2026 18:06:50 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagAXFixHydratedWidgetsParams2_Staged removed (was true;SteadyState;10;30;Revert;2026-01-21T17:32:51) | Mechanism: Fixes issues with how widget parameters are processed in the system. | Purpose: Improves the performance and reliability of widgets for a smoother user experience.

## 534c7efaf - 2026-01-21 12:05:36 -0600 - 01/21/2026 12:05:35
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 0c25bb1538fae7dcb1412e476404988dbd90b032 to a06256709be781419b87b94936884796be68846b | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 17:58:31 to 01/21/2026 18:04:51 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 0c25bb1538fae7dcb1412e476404988dbd90b032 to a06256709be781419b87b94936884796be68846b | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 17:58:31 to 01/21/2026 18:04:51 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFIntRobloxTelemetryBatchedReporterTimerIntervalMs_IXP removed (was 1;Portal.telemetry_v2_30_second_send-1768332428;telemetry_v2_30_second_send;2067951443;flagbank) | Mechanism: Sets the interval for batching telemetry reports in milliseconds. | Purpose: Optimizes performance by reducing the frequency of telemetry data sent, improving game efficiency.

## e6d7eb519 - 2026-01-21 12:01:08 -0600 - 01/21/2026 12:01:08
Added in Other:
- FFlagAddDisableHangReportingOnDebuggerBreak2_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T17:57:41 | Mechanism: Allows developers to disable reporting when the debugger is paused. | Purpose: Reduces unnecessary interruptions during debugging, making it smoother for developers.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from d9119cd57339b9620867de57d423e279188d0702 to 0c25bb1538fae7dcb1412e476404988dbd90b032 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 17:52:10 to 01/21/2026 17:58:31 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from d9119cd57339b9620867de57d423e279188d0702 to 0c25bb1538fae7dcb1412e476404988dbd90b032 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 17:52:10 to 01/21/2026 17:58:31 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 1376e1d7d - 2026-01-21 11:54:20 -0600 - 01/21/2026 11:54:20
Added in Other:
- FFlagSupportTerminalMilestoneInReactProfilerLogger_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T17:50:54 | Mechanism: Integrates terminal milestone tracking into the React profiler for performance analysis. | Purpose: Helps developers optimize game performance by providing better insights into application behavior.
- FFlagTelemetryCacheTrackBytes_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T17:50:57 | Mechanism: Tracks the amount of data used in telemetry more accurately. | Purpose: Helps developers understand data usage better, leading to improved game performance.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from d75deaab3bf66128104d2738d4800f389fa71d46 to d9119cd57339b9620867de57d423e279188d0702 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 17:49:28 to 01/21/2026 17:52:10 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from d75deaab3bf66128104d2738d4800f389fa71d46 to d9119cd57339b9620867de57d423e279188d0702 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 17:49:28 to 01/21/2026 17:52:10 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 58cd07fcc - 2026-01-21 11:52:03 -0600 - 01/21/2026 11:52:03
Changed in Other:
- DFFlagEnableLuaApiToRegisterEncryptedAssets_PlaceFilter changed from true;5646917919;5535247402;5650743011;5732185084;5796554295;5796546949;5796518985;5792232897;5790039516;5938526032;5180703112;5036207802;5947859215;5976554489;5967514178;5762783081;4927429832;5271804927;6225076142;6037119605;6313620339;5064251723;6409082143;6366043734;6366019895;5853107391;6303851272;6525184819;6462090760;6536060882;6656109940;6651400444;6833753645;6714103515;4640354700;537413528;6072880991;5388509011;6842406841;6763975907;6810569772;6836529297;5162124741;6242296404;893973440;6555759299;3272174207;2817429547;455327877;6923264315;6876683880;7085107422;6985067462;6994744290;6994747143;6994748760;6994750558;6999960212;7172485708;7085418723;7085416132;7085412189;7198250439;7236522784;7245550076;7234259327;7234162497;6679274937;3101667897;2913303231;364802243;815405518;277751860;6888253864;3457390032;4947425425;3689690770;756247480;285063827;5097010345;5111071793;7331970543;7277505766;7277502454;7277500013;7277498004;7277488595;6073366803;6764786757;5063122755;5579439108;698448212;706824758;447452406;5802642341;5233782396;7317639465;3475397644;4390337206;629119226;7489842410;5542348564;6774662981;7252283618;7021822357;7352428641;6782499449;7665856814;7665858439;7484857336;7429189755;7427268133;7619937171;7427270590;7280776979;7852580088;7711545622;7682549746;8519873016;8600776606;8430712643;8267821593;8523408215;8656125900;8656131552;8323392614;8209480473;8649501395;8526353932;8190625873;8451491417;8967359816;8430716410;8430720021;8691928149;8893378293;8893376837;8893375234;9230434873;9230346239;9244015146;6704278765;8528736393;8257697092;9288568020;9279671395;9426082120;9470653946;9379021494;9432710689;9424457125;4672922401;8583038000;4448566543;4543144283;4042427666;253431746;5974747216;6594198779;2533391464;8020984414;680750021;8778105026;5552313358;9297923091;6933439918;3956818381;4209071254;3623096087;3947737541;8983893891;9272701767;5074204685;5113678354;5089420081;5113680396;5101838579;5445525505;5237652005;6479720355;6152695332;9386500519;8988878415;5205771996;844441865;9449357539;9449346312;9449322773;9449312253;9449300051;5578992252;2056597445;9604473769;9666345834;9670497620;6536120621;9724177376;9769345912;4850718823;9300407930;6639766;6737970321;6599438732;9800475426;9291030453;9411975514;9648880560;9542881071;9552022794;9648883891;9648888455;9660279665;9708947809;9809534920;9463737803;9862870352;9862849972;9862789592;9894900344;9479367099;9486506804;9922817401;10002051672;10001920797;9982801024;9709393094;9659989778;9563367175;9997709290;10054526037;9465859374;9938883474;10113002281;10096544537;6445973668;6447798030;6996694685;8847312489;10190394336;10191408952;9423318797;10272293170;9314466589;10285554184;10057963710;10435224215;10146432319;10465853247;10465873968;9129288160;9134839143;9803810042;10201978992;10381578920;9717701801;9134941656;6837934317;9495369236;10217794885;10692093600;10695302524;10445615061;9524757503;10919330567;10895555747;10768305459;10912060909;11088788925;11110464593;11002897309;11116169215;11116168996;11116167810;11116167943;11109117989;10928399479;10966838056;10928411159;5289509545;4640368528;6023903686;11008022191;11138479969;11138508272;11115477432;11189492685;11189163544;11237748076;11237759266;11237755090;11237755215;11237755035;10894180429;10957579790;11315351400;11278516344;11286999367;11309534295;11287011130;11309714627;10695312682;11436221007;11444932478;11450899603;11497622549;11504321677;11498022323;11508738359;11508738629;11509888388;10720270804;9249776514;9049840490;9442460702;9280212924;8633070661;8472419479;11638764033;10126768872;11110455694;5326576507;5913722875;6386911572;8979173396;9125662619;9125667996;9916502094;11658541192;11105064323;10956766913;6737935903;9356050413;10900725936;11566389687;11566385150;11707114324;11697170413;11707130433;11707134020;11707136082;9616411936;11268121492;12113006580;12128024661;11504594758;12204626493;11946824905;3512481881;10752876846;9667175956;5938036553;11716079088;12331642939;11432287153;12268627706;12146837523;11302971424;12357661992;6766156863;12494616651;12202678406;4398851468;12670139300;12498843001;12519296046;12734535169;12734143030;12206689536;10762579692;11155913359;11758008778;12801867915;12955585971;12955639113;11777418254;12949951201;4580204640;6739798578;11840234178;11840243894;11849563578;11775512993;6350157277;5614144350;4111023553;5735553160;6032399813;6473861193;8668476218;4623386862;12983981151;10277607801;10277635599;10290363458;13022188319;12928836670;8665926945;12850021634;11808691145;12282826305;11377247691;8980446061;9346039031;2737661792;2871773892;3494556606;13413015814;2228128339;10048866629;4642718405;13166315054;12340070029;13388158627;13328383256;13602654181;7087982069;7226318833;12656847041;9607498518;7364683673;13408202978;9682240267;9346060856;13542186363;12566669965;12566670192;12566670531;12566670877;12566671127;12566671353;12566671529;12566671737;12566671942;12566672165;12566672378;12566672541;13671265268;13523140789;13413186900;13413150992;13190787726;13674000186;13539427431;13684472299;12108137135;12812062986;13581272176;13753433201;13539297457;13389095726;13260947739;12402722213;13324911372;13324917013;13403099993;4765976371;6507422231;13967475781;13104723083;7772134508;13978720221;13982397897;10211636793;12512626432;10894135377;14094603479;4996049426;10466293565;14112350669;14190161262;14190165276;13692908073;8003641817;11258371342;4014729424;14198802909;14050316710;6876897961;14298053780;14102374323;13913497984;13747937824;13279293321;14110497434;14550810567;3989527087;7830918930;14278574000;14618379101;4822723634;3386147714;14708622235;14708625196;14437915609;14702261217;14760955024;14106184172;14748762848;14700018413;14700503536;14700037385;14783054482;14700032079;14760646478;14700025324;14817872760;14100328983;14813042848;14745955429;14785438081;14889649635;14301956564;14263572229;10070780439;14478075491;14892572912;13279101556;13279104395;13279081722;13315930375;13433158135;14627078551;14898749542;14834598561;9979991670;14449036946;11806684300;12094311187;14968769349;2249956087;3670530550;903807016;9952774534;2534724415;6158369151;14890468710;11431489908;11240751480;11573230049;12804938725;11696224952;13326568190;8262636746;4823774310;4863502867;4692956554;14213578663;15018756870;15018759110;15019079127;15027905565;15090768015;15097774866;15121102278;13916945181;14042308512;13492762057;15154640283;14833076643;14565246812;14445068355;14445063204;13730658693;13730660420;13546112315;13324919767;5250557412;15229379003;14612279970;14520214356;15089099874;14618179455;14754487835;14976126374;15046883807;15220477368;13183511038;14884154051;12397515839;13886771215;15239190282;12661593618;13875657202;15230762576;7041939546;7061415250;15366303335;15360735397;14912173667;15246188138;14300294394;13978562365;13771684349;12631800770;12716371164;14042248442;11781338235;5972698540;1554960397;15148898765;15148887622;2274830359;5359990748;8003084678;15361532537;15548658643;11592468118;12572342856;12494782517;12596416224;12596420088;15559053838;15486683455;6804602922;6830203652;568350650;14184086618;15566395852;15565261877;4627817111;4627817882;4639006255;4674634750;4627871235;5045167247;14484579599;11383187368;11383187525;11383187688;11383188211;12275304058;15048215990;15230534913;15633063575;15633046194;15611620603;15872966840;15872999606;15883311692;15883312942;15883314575;15883381991;15035125923;14110608221;14110899148;14124909045;14308670761;6205205961;6364879587;6364881161;6391540653;6391642302;6463986562;6481131111;6507405695;6815760584;8709253565;15720304364;6413499953;15530488927;16006097169;6165038613;5785490105;5481779891;5481761946;5574814408;6238835427;6276061207;6517499261;6878610938;6866493186;7113825039;7116381283;7116702046;7116359883;7143609862;7409347440;7904559949;7904610383;7934323316;8232694369;8243032172;9405899288;9409201333;10430910649;11632100181;11632077138;11640052933;11793382673;11856129049;15705559027;15629541460;11632126721;8510589470;4241852625;8404684575;14238596528;15010814218;13184713709;13609999411;15696392675;15554979176;15555009597;15555152237;14696958202;5771467270;7308170886;5504135235;15918047570;3576787348;11863357640;12487789640;15123266349;16078980231;16078985058;16259243391;16199184400;16078983738;16256557884;16203696851;16258504798;16168372772;16256672025;16078982297;16289193441;11366343566;16283785212;15515633443;15432848623;15483728847;15015456533;16289193823;16351911381;5639479940;16013491402;5535744734;15553342068;5368632441;15513125039;5353488433;16462849084;16163726449;15481776731;14970015233;16465872867;15285658486;15574462881;16570021747;15254104733;844929123;166986752;16354460415;16537295657;14332741391;14345214315;14486832259;16628495726;13882183199;16447494654;15548888898;5721793369;5682917257;5363158649;15638731415;16866591880;16786806972;16805529755;16735914512;16719116735;16654319710;16646736918;16209331599;16565225470;15916274203;16252850662;16210529796;16185337739;16174846197;15354926906;15943789199;15544198652;15411224440;15370306777;15346604540;16806284145;16796346149;16732995612;16713027401;16296040578;16673347100;16970181235;16970189449;16970183654;16970185950;16970187260;16970191534;16970192771;16970193905;16637432168;16660479433;13000007654;16460694373;16429345261;16800307723;16725378671;16379598396;15489966249;16796377224;17065989459;17088952586;16739990874;15872961954;16630328183;16499205169;17183094198;16640867537;14266068291;14303756636;14709768053;17256291280;17181515306;17256293951;17256296185;17256298653;17256301033;17256075762;17256096568;17256118997;17256143199;13800717766;16849012343;15479377118;15334341098;16871709896;17327040230;17327030059;16434644938;15538708440;12129789607;6377740507;17490721006;17488220782;17373029266;13421266463;14895087162;12985361032;12985341499;12363313138;14704943644;17269346759;17269340201;17269292417;17480205349;17575492616;17575497513;17076563795;17556040524;17556037890;17659529447;16369023184;16369025010;17332451684;17116212498;16297600456;15992589987;15622887088;15164938644;17269297441;17336468238;17336471113;17336471400;17727263108;17727262816;17727262513;17727262301;17727205351;17727205123;17727204955;17727204653;17480206543;17563605831;17563608327;17563610497;16288561317;15218427871;15357970630;6934310111;14051757935;16017695597;17077627629;17356064588;16647545765;13398434647;13398230007;16890428355;13176058901;17569162537;17600179329;17600190676;17811870593;17495653641;17101171811;5970984243;14448662003;17447213133;18121514822;15218407500;17083366577;15843953438;15843957836;15843961264;17067024883;18341914628;17718083590;17576185251;17577101777;18195358934;18223727140;5297405973;18513265196;17578715653;17578711181;8737602449;8943844393;15611066348;14569410003;13415640045;14926164818;14879081274;8034026074;17811071580;18296260757;18112157688;17811079407;18111172516;18605830527;18397110912;18727659869;18503770332;18395887647;18536844330;18134433503;9859576867;8712817601;18734197659;14409368297;18654827953;18820482579;18727723068;18849518367;15486520864;18849588189;18849588625;18849589457;18963014717;14055498520;14891410939;18995954092;16110149934;19002847336;17230784439;18657144315;99590779149212;539960592;13691484057;15687370918;14775339176;2414851778;6052033819;4107728990;14943334555;2506552320;2727067538;2978693500;3582895165;2727072708;3165900886;3029833262;3383444582;3180260667;3885726701;3876515985;3994953548;3868367216;4050468028;3964647716;4310463616;2801784955;2978696440;4201860144;4310464656;4202491340;4310476380;4202709630;4310478830;4202959435;4310785330;4202976484;4310463940;3313821175;4465987684;4750776109;4465989998;4332744642;4465989351;4426374899;4465988196;4434431676;4526768266;15497256167;4617426261;4602326358;4646475570;4599453198;4646473427;4597651359;4646472003;3441138667;4646475342;3269109671;5703355191;5033247187;5703353651;5408429442;6075085184;5893171846;6075083204;6032934718;6386112652;6333155637;6510862058;6404275837;6510868181;6467448211;6847035264;6531678809;6847034886;6745424367;7071564842;6860483493;7499964980;131022574358785;9944262922;9171204517;10089970465;9649635544;9944263348;9649638002;10014664329;9863480370;10651517727;10074837226;10651527284;10489805577;10727165164;10683162998;10795158121;10724045559;11466514043;11155720733;11533444995;11379954422;11644048314;11530295305;14914684761;13741906191;13988110964;13661903549;14400549310;14213731433;14914700740;14692530018;14914855930;14768473411;15121292578;15025509897;75540798045662;122219842181820;125645867930579;18937883985;6101365417;6451702585;6454068948;3378819821;605887098;1701623492;3237615544;3367801828;18532003409;18228802662;18228805769;100219516754540;17808780506;87641067978449;111038871669535;8953242851;79765542592794;13423217832;134964516922646;5968388453;15855634668;16003793902;7305309231;15893203988;16033532219;126259681759948;17656935206;89410048034357;8472851459;8916037983;4954752502;79710108840469;11572762117;17670743999;71367782943796;16549917043;16703458787;132007474810089;18973713348;18139069423;13451596695;18440166505;12177325772;96695025808213;135229885104482;83692298883909;6073537839;88817926315458;104729035207525;76626266837363;113487357420897;107879176226772;130871423490486;11137575513;12943247001;12943245078;80005067957132;3818155097;3647333358;10324346056;10324347967;10662542523;10808838353;11353528705;96537472072550;99214917572799;18860937012;18860985311;115513358987315;129543795429973;18860934161;18860987667;17731318051;138811103914348;16732694052;131579468225600;11765402359;11828796994;5324719298;5342986949;6758497682;73848637067536;14900087266;119794400485251;80450830186028;88311415897149;119410252629691;103823923570615;110371647221022;96418538200619;7051736361;114220575509759;79372260836317;115243862171595;74712767707170;18752369972;129681463747237;78914719040186;15871955418;76762995566774;12641272458;6939111033;6426944918;137544427935459;15032994029;118706441243120;13389049867;10760024537;9281034297;15218831594;113029417107834;139040426524819;107286136869541;16126108459;14913354249;81793885962794;118556668407391;18647920435;88364323402553;109285335492645;128621093194805;123662243100680;112642345119817;18647956169;104526133535566;90753913217772;89161734699335;137461635848196;116697817957558;5750914919;6756890519;96005412559462;2548976609;2546612479;114907227214588;89227693986075;88342891966226;140080535032062;72073166002331;77221396426833;81319559867791;81737495082190;85341391356499;87351379991751;89712649086456;92911136919199;95324606076674;102435660805182;103275072481933;108343132674489;113050446018685;117785409277711;124000207868671;125165007426523;126865137021740;131981552061642;132643889235480;18668065416;92517437168342;99999183305180;115110570222234;73425816668928;88233429548268;130739873848552;82710350236919;71580765918830;94170955089948;16909704232;101394944107806;104746643025210;119038667082595;95448143850147;139548786112139;96804383423412;124660577261950;122819728171185;132004114310511;787988004728135;129230994638464;73708914208963;98118902024430;132935874487897;90216279544722;77915441816737;87014900491609;79018097401349;85774300903718;120428153057168;97872047573441;134772811582797;72534188920161;138993958163764;102018283146594;78037392664516;79895744759186;117860234965291;125337041623563;17840501830;72190557439380;70454767164205;91733245171139;91228542222122;130888608591113;124948436023758;7450497506;75663528075786;118304171612688;79174624435953;116296033709863;83545284007309;130651760577349;122825844998639;135381296103877;96265145951044;78026056611611;7720048224;96077916226556;97056995744329;100277824753624;103793593586394;138811411414576;12640491155;125889350453386;16590754220;16978845877;80611835622737;102716401412280;96902541318046;15351762625;13772394625;14486733015;127966866038346;125654797564410;125247930279216;107447262204970;89872700617308;111865923474705;14368557094;14732610803;14907104587;14915220621;15092011734;15106881665;15131065025;15131070225;15144787112;15181537975;15185247558;15227672707;15229817314;15234596844;15264892126;15351763826;15351764032;15351764187;15351764348;15351764507;15351764740;15351764881;15351764966;15351765130;15462212483;15509346379;15509350986;15509357472;15517169103;15552588346;15552625961;15582813408;15582821022;15582823307;15582834071;15582835531;16031521714;16031541538;16044264830;16281300371;16331595046;16331596518;16331598816;16331600459;16331633255;16331634414;16331635718;16331635995;16456370330;16581613207;16581637217;16581648071;17757578266;17757592456;75474715372485;80316691895873;92458008626219;94739503741288;84211911194381;86959746238096;79152141768156;133468541502594;78575159450955;80951765302134;105378961467772;89865052230260;81090934593448;75313569154781;89596436703421;92752656404044;126581936679803;107738647542786;10489114145;9872472334;121271605799901;17069498206;16931515487;16896790433;11761274032;11764980869;16926077853;11753029192;13965228772;102916117017468;121372427435947;119952687833295;112898865140956;124044706645343;135456035952103;93804003372568;124248440864832;18334179599;16389395869;16844101122;76603224491021;83370733060419;103479080416741;101128307729202;107731702241186;122645084125812;78529064493417;130112681881594;139392011420826;115700747039144;78517252105400;73484909444934;114347154312193;74815645991109;18248633989;17698425045;86098085533596;118758941554698;17750719380;96628744411718;113567868263978;74475530512823;128778160701214;140223498612774;125156298745329;118535429818702;89703062547673;103883018654651;140287841692914;3010276628;111014975161818;102605854369937;11158043705;17747224478;102730218405996;104676452414043;119369863786092;118524425609297;86955381046056;8472085082;90203410635303;72723436074493;110708547231329;103650844120570;87868857007174;93481552663411;112564920810158;109983668079237;96342491571673;128762245270197;120148879522453;73226809349189;119602771011506;127732283735594;125461249438738;87445296052708;136517679309458;15768329004;108059757699905;70542636057631;101606960500983;103349603274756;89343390950953;93651812913748;15101393044;15642262165;15642275269;17481176031;89606894431558;127076465038391;93577264377184;91732685148261;138937299583930;78572645499619;122061917549078;106153673498996;95047916580305;133400153206637;110470525256662;123468479998097;82441850250520;116185509299834;81072337989394;96652240771528;98881331868329;108204315743653;109533232275124;121269997456920;124184374777402;111145810816450;3233351170;8458974184;72178041068475;130859235108277;86962954395779;77162302089899;6931042565;134314141048307;109684591839194;74691681039273;73956553001240;96802054849934;86789627188240;79136731857959;103521881639626;117134837736236;7099263384;93507193197337;127230203073079;70882603136659;127978196002690;77569554466776;128311527873732;80289684342936;122273223414774;78499094786141;107214420833891;133370458228346;90688392698752;89752387031554;103658027677245;105764668548382;87706612753421;128997103569769;96223451292903;96604744451060;95445450782680;90346996348563;76800900334648;131082319718215;110321186768296;8248004705;119058117746091;95815562184695;72293243384445;140159579197170;120064291937900;107757296388993;140104197573447;124991631436250;72277410833409;87773427230428;82298052173374;122241151273608;112849554065563;75333462792994;130160244117542;74185370550900;86517463532234;118814182678109;93561553871338;108462619394007;14021953565;124087144919678;123439661582156;124532804761244;100349497885381;127104365805084;126953033317926;106560355070751;140358213724897;114181481862155;80010340277260;140429793519388;134497530231879;136409236554789;86522549610893;95656979989750;71683821699644;85265340826775;121928784820997;77638307191108;92626170235541;104548429314536;6325068386;80219362391408;129027544628653;115594497201999;103332930661641;72921500494845;139434932554684;136505972636980;94991053520125;72995931205549;108862151633853;5901440255;6119570238;6126992207;105814505642482;74588338744555;97589732026842;85513756910439;93366760336122;77977481651141;17026065260;17026079202;17026081473;17026082885;17026083128;17026083473;17026083734;17026084038;17026084803;17026085546;17671143350;17671143714;17671144394;17671148230;18605534919;116238950016910;129525666081265;2338325648;4822225642;4940687511;7097139127;7098347455;7098347570;11414445247;12770493773;12986634964;12986636453;12986638725;13415948659;13834702475;14801724413;15098628040;17685156577;17685159087;17685161741;17685164681;17685181130;93001350941802;125444254609144;124335066106952;4924922222;11981280399;12446587737;4566572536;91751877679930;126884695634066;140398800602847;96443646410175;84663621619610;138349771708864;131456775839122;138137777772420;134614543668802;79368714145670;132151526704941;92106543276146;98573759838033;110125451314286;115600257231423;95183590295663;81493541492179;85239275355743;16625391970;18650866518;18895717031;11452349236;80951089371762;5136040124;5136248000;3405618667;3523688332;3237397989;3474940993;3975583821;4994548435;6281216515;4179732320;6902944446;9053214954;70876832253163;133377094302868;128842011385105;140202562685639;16448271523;17168246061;89121255316677;137212977957030;71700852488818;101856043486797;74125567120998;109180942748509;77677109342572;83255568226634;93809530689375;76247082393051;74702364775128;118168745564002;138161860713168;93680175266457;137371839632687;93054971012433;98176833880009;127773181414564;99955340962947;85558630854255;78691859768596;120392838716850;81914282243912;136954310107221;87939894615077;130815519916065;96668462040940;72741786721483;98798461601883;118806061296143;94911460762869;140422012851942;75107512524289;87647277375829;75126364120046;115843826901665;94859564409757;77155705414604;139990231502528;123780435956703;104926345480848;124398716501784;89201738681342;78055502212608;131716211654599;112780263016678;99519129453387;85316963135218;110229398924353;123632192357489;136031805345492;123563444866327;132807925060015;72975517268088;123921593837160;103984222380370;101949297449238;95294502234968;122576696342824;97136653744938;87876279581635;129711915886715;135427513412109;18799085098;125182893468913;109263383287853;111448836804180 to true;5646917919;5535247402;5650743011;5732185084;5796554295;5796546949;5796518985;5792232897;5790039516;5938526032;5180703112;5036207802;5947859215;5976554489;5967514178;5762783081;4927429832;5271804927;6225076142;6037119605;6313620339;5064251723;6409082143;6366043734;6366019895;5853107391;6303851272;6525184819;6462090760;6536060882;6656109940;6651400444;6833753645;6714103515;4640354700;537413528;6072880991;5388509011;6842406841;6763975907;6810569772;6836529297;5162124741;6242296404;893973440;6555759299;3272174207;2817429547;455327877;6923264315;6876683880;7085107422;6985067462;6994744290;6994747143;6994748760;6994750558;6999960212;7172485708;7085418723;7085416132;7085412189;7198250439;7236522784;7245550076;7234259327;7234162497;6679274937;3101667897;2913303231;364802243;815405518;277751860;6888253864;3457390032;4947425425;3689690770;756247480;285063827;5097010345;5111071793;7331970543;7277505766;7277502454;7277500013;7277498004;7277488595;6073366803;6764786757;5063122755;5579439108;698448212;706824758;447452406;5802642341;5233782396;7317639465;3475397644;4390337206;629119226;7489842410;5542348564;6774662981;7252283618;7021822357;7352428641;6782499449;7665856814;7665858439;7484857336;7429189755;7427268133;7619937171;7427270590;7280776979;7852580088;7711545622;7682549746;8519873016;8600776606;8430712643;8267821593;8523408215;8656125900;8656131552;8323392614;8209480473;8649501395;8526353932;8190625873;8451491417;8967359816;8430716410;8430720021;8691928149;8893378293;8893376837;8893375234;9230434873;9230346239;9244015146;6704278765;8528736393;8257697092;9288568020;9279671395;9426082120;9470653946;9379021494;9432710689;9424457125;4672922401;8583038000;4448566543;4543144283;4042427666;253431746;5974747216;6594198779;2533391464;8020984414;680750021;8778105026;5552313358;9297923091;6933439918;3956818381;4209071254;3623096087;3947737541;8983893891;9272701767;5074204685;5113678354;5089420081;5113680396;5101838579;5445525505;5237652005;6479720355;6152695332;9386500519;8988878415;5205771996;844441865;9449357539;9449346312;9449322773;9449312253;9449300051;5578992252;2056597445;9604473769;9666345834;9670497620;6536120621;9724177376;9769345912;4850718823;9300407930;6639766;6737970321;6599438732;9800475426;9291030453;9411975514;9648880560;9542881071;9552022794;9648883891;9648888455;9660279665;9708947809;9809534920;9463737803;9862870352;9862849972;9862789592;9894900344;9479367099;9486506804;9922817401;10002051672;10001920797;9982801024;9709393094;9659989778;9563367175;9997709290;10054526037;9465859374;9938883474;10113002281;10096544537;6445973668;6447798030;6996694685;8847312489;10190394336;10191408952;9423318797;10272293170;9314466589;10285554184;10057963710;10435224215;10146432319;10465853247;10465873968;9129288160;9134839143;9803810042;10201978992;10381578920;9717701801;9134941656;6837934317;9495369236;10217794885;10692093600;10695302524;10445615061;9524757503;10919330567;10895555747;10768305459;10912060909;11088788925;11110464593;11002897309;11116169215;11116168996;11116167810;11116167943;11109117989;10928399479;10966838056;10928411159;5289509545;4640368528;6023903686;11008022191;11138479969;11138508272;11115477432;11189492685;11189163544;11237748076;11237759266;11237755090;11237755215;11237755035;10894180429;10957579790;11315351400;11278516344;11286999367;11309534295;11287011130;11309714627;10695312682;11436221007;11444932478;11450899603;11497622549;11504321677;11498022323;11508738359;11508738629;11509888388;10720270804;9249776514;9049840490;9442460702;9280212924;8633070661;8472419479;11638764033;10126768872;11110455694;5326576507;5913722875;6386911572;8979173396;9125662619;9125667996;9916502094;11658541192;11105064323;10956766913;6737935903;9356050413;10900725936;11566389687;11566385150;11707114324;11697170413;11707130433;11707134020;11707136082;9616411936;11268121492;12113006580;12128024661;11504594758;12204626493;11946824905;3512481881;10752876846;9667175956;5938036553;11716079088;12331642939;11432287153;12268627706;12146837523;11302971424;12357661992;6766156863;12494616651;12202678406;4398851468;12670139300;12498843001;12519296046;12734535169;12734143030;12206689536;10762579692;11155913359;11758008778;12801867915;12955585971;12955639113;11777418254;12949951201;4580204640;6739798578;11840234178;11840243894;11849563578;11775512993;6350157277;5614144350;4111023553;5735553160;6032399813;6473861193;8668476218;4623386862;12983981151;10277607801;10277635599;10290363458;13022188319;12928836670;8665926945;12850021634;11808691145;12282826305;11377247691;8980446061;9346039031;2737661792;2871773892;3494556606;13413015814;2228128339;10048866629;4642718405;13166315054;12340070029;13388158627;13328383256;13602654181;7087982069;7226318833;12656847041;9607498518;7364683673;13408202978;9682240267;9346060856;13542186363;12566669965;12566670192;12566670531;12566670877;12566671127;12566671353;12566671529;12566671737;12566671942;12566672165;12566672378;12566672541;13671265268;13523140789;13413186900;13413150992;13190787726;13674000186;13539427431;13684472299;12108137135;12812062986;13581272176;13753433201;13539297457;13389095726;13260947739;12402722213;13324911372;13324917013;13403099993;4765976371;6507422231;13967475781;13104723083;7772134508;13978720221;13982397897;10211636793;12512626432;10894135377;14094603479;4996049426;10466293565;14112350669;14190161262;14190165276;13692908073;8003641817;11258371342;4014729424;14198802909;14050316710;6876897961;14298053780;14102374323;13913497984;13747937824;13279293321;14110497434;14550810567;3989527087;7830918930;14278574000;14618379101;4822723634;3386147714;14708622235;14708625196;14437915609;14702261217;14760955024;14106184172;14748762848;14700018413;14700503536;14700037385;14783054482;14700032079;14760646478;14700025324;14817872760;14100328983;14813042848;14745955429;14785438081;14889649635;14301956564;14263572229;10070780439;14478075491;14892572912;13279101556;13279104395;13279081722;13315930375;13433158135;14627078551;14898749542;14834598561;9979991670;14449036946;11806684300;12094311187;14968769349;2249956087;3670530550;903807016;9952774534;2534724415;6158369151;14890468710;11431489908;11240751480;11573230049;12804938725;11696224952;13326568190;8262636746;4823774310;4863502867;4692956554;14213578663;15018756870;15018759110;15019079127;15027905565;15090768015;15097774866;15121102278;13916945181;14042308512;13492762057;15154640283;14833076643;14565246812;14445068355;14445063204;13730658693;13730660420;13546112315;13324919767;5250557412;15229379003;14612279970;14520214356;15089099874;14618179455;14754487835;14976126374;15046883807;15220477368;13183511038;14884154051;12397515839;13886771215;15239190282;12661593618;13875657202;15230762576;7041939546;7061415250;15366303335;15360735397;14912173667;15246188138;14300294394;13978562365;13771684349;12631800770;12716371164;14042248442;11781338235;5972698540;1554960397;15148898765;15148887622;2274830359;5359990748;8003084678;15361532537;15548658643;11592468118;12572342856;12494782517;12596416224;12596420088;15559053838;15486683455;6804602922;6830203652;568350650;14184086618;15566395852;15565261877;4627817111;4627817882;4639006255;4674634750;4627871235;5045167247;14484579599;11383187368;11383187525;11383187688;11383188211;12275304058;15048215990;15230534913;15633063575;15633046194;15611620603;15872966840;15872999606;15883311692;15883312942;15883314575;15883381991;15035125923;14110608221;14110899148;14124909045;14308670761;6205205961;6364879587;6364881161;6391540653;6391642302;6463986562;6481131111;6507405695;6815760584;8709253565;15720304364;6413499953;15530488927;16006097169;6165038613;5785490105;5481779891;5481761946;5574814408;6238835427;6276061207;6517499261;6878610938;6866493186;7113825039;7116381283;7116702046;7116359883;7143609862;7409347440;7904559949;7904610383;7934323316;8232694369;8243032172;9405899288;9409201333;10430910649;11632100181;11632077138;11640052933;11793382673;11856129049;15705559027;15629541460;11632126721;8510589470;4241852625;8404684575;14238596528;15010814218;13184713709;13609999411;15696392675;15554979176;15555009597;15555152237;14696958202;5771467270;7308170886;5504135235;15918047570;3576787348;11863357640;12487789640;15123266349;16078980231;16078985058;16259243391;16199184400;16078983738;16256557884;16203696851;16258504798;16168372772;16256672025;16078982297;16289193441;11366343566;16283785212;15515633443;15432848623;15483728847;15015456533;16289193823;16351911381;5639479940;16013491402;5535744734;15553342068;5368632441;15513125039;5353488433;16462849084;16163726449;15481776731;14970015233;16465872867;15285658486;15574462881;16570021747;15254104733;844929123;166986752;16354460415;16537295657;14332741391;14345214315;14486832259;16628495726;13882183199;16447494654;15548888898;5721793369;5682917257;5363158649;15638731415;16866591880;16786806972;16805529755;16735914512;16719116735;16654319710;16646736918;16209331599;16565225470;15916274203;16252850662;16210529796;16185337739;16174846197;15354926906;15943789199;15544198652;15411224440;15370306777;15346604540;16806284145;16796346149;16732995612;16713027401;16296040578;16673347100;16970181235;16970189449;16970183654;16970185950;16970187260;16970191534;16970192771;16970193905;16637432168;16660479433;13000007654;16460694373;16429345261;16800307723;16725378671;16379598396;15489966249;16796377224;17065989459;17088952586;16739990874;15872961954;16630328183;16499205169;17183094198;16640867537;14266068291;14303756636;14709768053;17256291280;17181515306;17256293951;17256296185;17256298653;17256301033;17256075762;17256096568;17256118997;17256143199;13800717766;16849012343;15479377118;15334341098;16871709896;17327040230;17327030059;16434644938;15538708440;12129789607;6377740507;17490721006;17488220782;17373029266;13421266463;14895087162;12985361032;12985341499;12363313138;14704943644;17269346759;17269340201;17269292417;17480205349;17575492616;17575497513;17076563795;17556040524;17556037890;17659529447;16369023184;16369025010;17332451684;17116212498;16297600456;15992589987;15622887088;15164938644;17269297441;17336468238;17336471113;17336471400;17727263108;17727262816;17727262513;17727262301;17727205351;17727205123;17727204955;17727204653;17480206543;17563605831;17563608327;17563610497;16288561317;15218427871;15357970630;6934310111;14051757935;16017695597;17077627629;17356064588;16647545765;13398434647;13398230007;16890428355;13176058901;17569162537;17600179329;17600190676;17811870593;17495653641;17101171811;5970984243;14448662003;17447213133;18121514822;15218407500;17083366577;15843953438;15843957836;15843961264;17067024883;18341914628;17718083590;17576185251;17577101777;18195358934;18223727140;5297405973;18513265196;17578715653;17578711181;8737602449;8943844393;15611066348;14569410003;13415640045;14926164818;14879081274;8034026074;17811071580;18296260757;18112157688;17811079407;18111172516;18605830527;18397110912;18727659869;18503770332;18395887647;18536844330;18134433503;9859576867;8712817601;18734197659;14409368297;18654827953;18820482579;18727723068;18849518367;15486520864;18849588189;18849588625;18849589457;18963014717;14055498520;14891410939;18995954092;16110149934;19002847336;17230784439;18657144315;99590779149212;539960592;13691484057;15687370918;14775339176;2414851778;6052033819;4107728990;14943334555;2506552320;2727067538;2978693500;3582895165;2727072708;3165900886;3029833262;3383444582;3180260667;3885726701;3876515985;3994953548;3868367216;4050468028;3964647716;4310463616;2801784955;2978696440;4201860144;4310464656;4202491340;4310476380;4202709630;4310478830;4202959435;4310785330;4202976484;4310463940;3313821175;4465987684;4750776109;4465989998;4332744642;4465989351;4426374899;4465988196;4434431676;4526768266;15497256167;4617426261;4602326358;4646475570;4599453198;4646473427;4597651359;4646472003;3441138667;4646475342;3269109671;5703355191;5033247187;5703353651;5408429442;6075085184;5893171846;6075083204;6032934718;6386112652;6333155637;6510862058;6404275837;6510868181;6467448211;6847035264;6531678809;6847034886;6745424367;7071564842;6860483493;7499964980;131022574358785;9944262922;9171204517;10089970465;9649635544;9944263348;9649638002;10014664329;9863480370;10651517727;10074837226;10651527284;10489805577;10727165164;10683162998;10795158121;10724045559;11466514043;11155720733;11533444995;11379954422;11644048314;11530295305;14914684761;13741906191;13988110964;13661903549;14400549310;14213731433;14914700740;14692530018;14914855930;14768473411;15121292578;15025509897;75540798045662;122219842181820;125645867930579;18937883985;6101365417;6451702585;6454068948;3378819821;605887098;1701623492;3237615544;3367801828;18532003409;18228802662;18228805769;100219516754540;17808780506;87641067978449;111038871669535;8953242851;79765542592794;13423217832;134964516922646;5968388453;15855634668;16003793902;7305309231;15893203988;16033532219;126259681759948;17656935206;89410048034357;8472851459;8916037983;4954752502;79710108840469;11572762117;17670743999;71367782943796;16549917043;16703458787;132007474810089;18973713348;18139069423;13451596695;18440166505;12177325772;96695025808213;135229885104482;83692298883909;6073537839;88817926315458;104729035207525;76626266837363;113487357420897;107879176226772;130871423490486;11137575513;12943247001;12943245078;80005067957132;3818155097;3647333358;10324346056;10324347967;10662542523;10808838353;11353528705;96537472072550;99214917572799;18860937012;18860985311;115513358987315;129543795429973;18860934161;18860987667;17731318051;138811103914348;16732694052;131579468225600;11765402359;11828796994;5324719298;5342986949;6758497682;73848637067536;14900087266;119794400485251;80450830186028;88311415897149;119410252629691;103823923570615;110371647221022;96418538200619;7051736361;114220575509759;79372260836317;115243862171595;74712767707170;18752369972;129681463747237;78914719040186;15871955418;76762995566774;12641272458;6939111033;6426944918;137544427935459;15032994029;118706441243120;13389049867;10760024537;9281034297;15218831594;113029417107834;139040426524819;107286136869541;16126108459;14913354249;81793885962794;118556668407391;18647920435;88364323402553;109285335492645;128621093194805;123662243100680;112642345119817;18647956169;104526133535566;90753913217772;89161734699335;137461635848196;116697817957558;5750914919;6756890519;96005412559462;2548976609;2546612479;114907227214588;89227693986075;88342891966226;140080535032062;72073166002331;77221396426833;81319559867791;81737495082190;85341391356499;87351379991751;89712649086456;92911136919199;95324606076674;102435660805182;103275072481933;108343132674489;113050446018685;117785409277711;124000207868671;125165007426523;126865137021740;131981552061642;132643889235480;18668065416;92517437168342;99999183305180;115110570222234;73425816668928;88233429548268;130739873848552;82710350236919;71580765918830;94170955089948;16909704232;101394944107806;104746643025210;119038667082595;95448143850147;139548786112139;96804383423412;124660577261950;122819728171185;132004114310511;787988004728135;129230994638464;73708914208963;98118902024430;132935874487897;90216279544722;77915441816737;87014900491609;79018097401349;85774300903718;120428153057168;97872047573441;134772811582797;72534188920161;138993958163764;102018283146594;78037392664516;79895744759186;117860234965291;125337041623563;17840501830;72190557439380;70454767164205;91733245171139;91228542222122;130888608591113;124948436023758;7450497506;75663528075786;118304171612688;79174624435953;116296033709863;83545284007309;130651760577349;122825844998639;135381296103877;96265145951044;78026056611611;7720048224;96077916226556;97056995744329;100277824753624;103793593586394;138811411414576;12640491155;125889350453386;16590754220;16978845877;80611835622737;102716401412280;96902541318046;15351762625;13772394625;14486733015;127966866038346;125654797564410;125247930279216;107447262204970;89872700617308;111865923474705;14368557094;14732610803;14907104587;14915220621;15092011734;15106881665;15131065025;15131070225;15144787112;15181537975;15185247558;15227672707;15229817314;15234596844;15264892126;15351763826;15351764032;15351764187;15351764348;15351764507;15351764740;15351764881;15351764966;15351765130;15462212483;15509346379;15509350986;15509357472;15517169103;15552588346;15552625961;15582813408;15582821022;15582823307;15582834071;15582835531;16031521714;16031541538;16044264830;16281300371;16331595046;16331596518;16331598816;16331600459;16331633255;16331634414;16331635718;16331635995;16456370330;16581613207;16581637217;16581648071;17757578266;17757592456;75474715372485;80316691895873;92458008626219;94739503741288;84211911194381;86959746238096;79152141768156;133468541502594;78575159450955;80951765302134;105378961467772;89865052230260;81090934593448;75313569154781;89596436703421;92752656404044;126581936679803;107738647542786;10489114145;9872472334;121271605799901;17069498206;16931515487;16896790433;11761274032;11764980869;16926077853;11753029192;13965228772;102916117017468;121372427435947;119952687833295;112898865140956;124044706645343;135456035952103;93804003372568;124248440864832;18334179599;16389395869;16844101122;76603224491021;83370733060419;103479080416741;101128307729202;107731702241186;122645084125812;78529064493417;130112681881594;139392011420826;115700747039144;78517252105400;73484909444934;114347154312193;74815645991109;18248633989;17698425045;86098085533596;118758941554698;17750719380;96628744411718;113567868263978;74475530512823;128778160701214;140223498612774;125156298745329;118535429818702;89703062547673;103883018654651;140287841692914;3010276628;111014975161818;102605854369937;11158043705;17747224478;102730218405996;104676452414043;119369863786092;118524425609297;86955381046056;8472085082;90203410635303;72723436074493;110708547231329;103650844120570;87868857007174;93481552663411;112564920810158;109983668079237;96342491571673;128762245270197;120148879522453;73226809349189;119602771011506;127732283735594;125461249438738;87445296052708;136517679309458;15768329004;108059757699905;70542636057631;101606960500983;103349603274756;89343390950953;93651812913748;15101393044;15642262165;15642275269;17481176031;89606894431558;127076465038391;93577264377184;91732685148261;138937299583930;78572645499619;122061917549078;106153673498996;95047916580305;133400153206637;110470525256662;123468479998097;82441850250520;116185509299834;81072337989394;96652240771528;98881331868329;108204315743653;109533232275124;121269997456920;124184374777402;111145810816450;3233351170;8458974184;72178041068475;130859235108277;86962954395779;77162302089899;6931042565;134314141048307;109684591839194;74691681039273;73956553001240;96802054849934;86789627188240;79136731857959;103521881639626;117134837736236;7099263384;93507193197337;127230203073079;70882603136659;127978196002690;77569554466776;128311527873732;80289684342936;122273223414774;78499094786141;107214420833891;133370458228346;90688392698752;89752387031554;103658027677245;105764668548382;87706612753421;128997103569769;96223451292903;96604744451060;95445450782680;90346996348563;76800900334648;131082319718215;110321186768296;8248004705;119058117746091;95815562184695;72293243384445;140159579197170;120064291937900;107757296388993;140104197573447;124991631436250;72277410833409;87773427230428;82298052173374;122241151273608;112849554065563;75333462792994;130160244117542;74185370550900;86517463532234;118814182678109;93561553871338;108462619394007;14021953565;124087144919678;123439661582156;124532804761244;100349497885381;127104365805084;126953033317926;106560355070751;140358213724897;114181481862155;80010340277260;140429793519388;134497530231879;136409236554789;86522549610893;95656979989750;71683821699644;85265340826775;121928784820997;77638307191108;92626170235541;104548429314536;6325068386;80219362391408;129027544628653;115594497201999;103332930661641;72921500494845;139434932554684;136505972636980;94991053520125;72995931205549;108862151633853;5901440255;6119570238;6126992207;105814505642482;74588338744555;97589732026842;85513756910439;93366760336122;77977481651141;17026065260;17026079202;17026081473;17026082885;17026083128;17026083473;17026083734;17026084038;17026084803;17026085546;17671143350;17671143714;17671144394;17671148230;18605534919;116238950016910;129525666081265;2338325648;4822225642;4940687511;7097139127;7098347455;7098347570;11414445247;12770493773;12986634964;12986636453;12986638725;13415948659;13834702475;14801724413;15098628040;17685156577;17685159087;17685161741;17685164681;17685181130;93001350941802;125444254609144;124335066106952;4924922222;11981280399;12446587737;4566572536;91751877679930;126884695634066;140398800602847;96443646410175;84663621619610;138349771708864;131456775839122;138137777772420;134614543668802;79368714145670;132151526704941;92106543276146;98573759838033;110125451314286;115600257231423;95183590295663;81493541492179;85239275355743;16625391970;18650866518;18895717031;11452349236;80951089371762;5136040124;5136248000;3405618667;3523688332;3237397989;3474940993;3975583821;4994548435;6281216515;4179732320;6902944446;9053214954;70876832253163;133377094302868;128842011385105;140202562685639;16448271523;17168246061;89121255316677;137212977957030;71700852488818;101856043486797;74125567120998;109180942748509;77677109342572;83255568226634;93809530689375;76247082393051;74702364775128;118168745564002;138161860713168;93680175266457;137371839632687;93054971012433;98176833880009;127773181414564;99955340962947;85558630854255;78691859768596;120392838716850;81914282243912;136954310107221;87939894615077;130815519916065;96668462040940;72741786721483;98798461601883;118806061296143;94911460762869;140422012851942;75107512524289;87647277375829;75126364120046;115843826901665;94859564409757;77155705414604;139990231502528;123780435956703;104926345480848;124398716501784;89201738681342;78055502212608;131716211654599;112780263016678;99519129453387;85316963135218;110229398924353;123632192357489;136031805345492;123563444866327;132807925060015;72975517268088;123921593837160;103984222380370;101949297449238;95294502234968;122576696342824;97136653744938;87876279581635;129711915886715;135427513412109;18799085098;125182893468913;109263383287853;111448836804180;101018932049972;82831869681936;108395470109881 | Mechanism: Allows Lua scripts to register encrypted assets with a filter for specific places. | Purpose: Enhances security and control over asset usage in different game environments.
- DFStringFlagRepoGitHashDynamicString changed from 46673d1aa831bba4debf663a80a66c672a379e65 to d75deaab3bf66128104d2738d4800f389fa71d46 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 17:49:09 to 01/21/2026 17:49:28 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 46673d1aa831bba4debf663a80a66c672a379e65 to d75deaab3bf66128104d2738d4800f389fa71d46 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 17:49:09 to 01/21/2026 17:49:28 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## b89cc1504 - 2026-01-21 11:49:47 -0600 - 01/21/2026 11:49:47
Added in Other:
- FFlagAddVideoDetectorWrapper_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T17:47:06 | Mechanism: Integrates a wrapper for detecting video content. | Purpose: Enhances the ability to manage and display video content in games.
Added in Camera/UI:
- FFlagSduiBadgeTileContained_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;308554894;2026-01-21T17:47:00 | Mechanism: Modifies how badge tiles are displayed in the user interface. | Purpose: Players can see their badges more clearly and access them more conveniently.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from cdc4b9eaf504d8e3a7ccea0a94cfe2fe0f2e473d to 46673d1aa831bba4debf663a80a66c672a379e65 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 17:46:45 to 01/21/2026 17:49:09 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from cdc4b9eaf504d8e3a7ccea0a94cfe2fe0f2e473d to 46673d1aa831bba4debf663a80a66c672a379e65 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 17:46:45 to 01/21/2026 17:49:09 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Changed in Camera/UI:
- FIntRelocateMobileMenuButtonsVariant_IXP changed from 1;UIEcosystem.User.Migration;UIEcosystem.User.Migration.ReactPeoplePageAndCardLayout2;398703262;flagbank to 1;UIEcosystem.User.Migration;UIEcosystem.User.Migration.ReactPeoplePageAndCardLayout2;1778374245;flagbank | Mechanism: Moves buttons in the mobile menu to a new layout. | Purpose: Improves navigation and accessibility for mobile players.

## d4698f5f2 - 2026-01-21 11:47:30 -0600 - 01/21/2026 11:47:30
Added in Camera/UI:
- FFlagRemoveExperienceMenuABTestManager_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;70130128;2026-01-21T17:46:08 | Mechanism: Removes the A/B testing manager for the experience menu. | Purpose: Simplifies the experience menu for players by removing unnecessary testing features.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from e94d09d594d421c84067731fb7b0447624e64e79 to cdc4b9eaf504d8e3a7ccea0a94cfe2fe0f2e473d | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 17:41:40 to 01/21/2026 17:46:45 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from e94d09d594d421c84067731fb7b0447624e64e79 to cdc4b9eaf504d8e3a7ccea0a94cfe2fe0f2e473d | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 17:41:40 to 01/21/2026 17:46:45 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 52ac5607a - 2026-01-21 11:43:00 -0600 - 01/21/2026 11:43:00
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from d623c4b76466eca3b724b787d51979f0dbd76a18 to e94d09d594d421c84067731fb7b0447624e64e79 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 17:40:16 to 01/21/2026 17:41:40 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from d623c4b76466eca3b724b787d51979f0dbd76a18 to e94d09d594d421c84067731fb7b0447624e64e79 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 17:40:16 to 01/21/2026 17:41:40 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## c662f52e3 - 2026-01-21 11:40:42 -0600 - 01/21/2026 11:40:42
Added in Other:
- FFlagFastVideoFrameSamplerSeek_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T17:38:20 | Mechanism: Enhances the speed at which video frames are sampled during playback. | Purpose: Provides a smoother video playback experience for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from adda46811bcb338107b40a0a03317300e7d76e03 to d623c4b76466eca3b724b787d51979f0dbd76a18 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 17:37:31 to 01/21/2026 17:40:16 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from adda46811bcb338107b40a0a03317300e7d76e03 to d623c4b76466eca3b724b787d51979f0dbd76a18 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 17:37:31 to 01/21/2026 17:40:16 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Network:
- SFFlagIAS_InstancePointersHoldAcrossReplication3_Staged removed (was true;SteadyState;10;30;Revert;2026-01-21T17:36:43) | Mechanism: Maintains references to game objects during data updates. | Purpose: Ensures smoother gameplay and object interactions for players.

## 5acad87ee - 2026-01-21 11:38:27 -0600 - 01/21/2026 11:38:27
Added in Network:
- SFFlagIAS_InstancePointersHoldAcrossReplication3_Staged = true;SteadyState;10;30;Revert;2026-01-21T17:36:43 | Mechanism: Maintains references to game objects during data updates. | Purpose: Ensures smoother gameplay and object interactions for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from c8b2599bb5cdb1f086e98394d1b642859cec19fa to adda46811bcb338107b40a0a03317300e7d76e03 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 17:33:48 to 01/21/2026 17:37:31 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from c8b2599bb5cdb1f086e98394d1b642859cec19fa to adda46811bcb338107b40a0a03317300e7d76e03 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 17:33:48 to 01/21/2026 17:37:31 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 5053a0e61 - 2026-01-21 11:36:14 -0600 - 01/21/2026 11:36:14
Added in Other:
- FFlagAXFixHydratedWidgetsParams2_Staged = true;SteadyState;10;30;Revert;2026-01-21T17:32:51 | Mechanism: Fixes issues with how widget parameters are processed in the system. | Purpose: Improves the performance and reliability of widgets for a smoother user experience.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 537602be5bd36fc9cd31b5d8c7dc97447e867148 to c8b2599bb5cdb1f086e98394d1b642859cec19fa | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 17:29:35 to 01/21/2026 17:33:48 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 537602be5bd36fc9cd31b5d8c7dc97447e867148 to c8b2599bb5cdb1f086e98394d1b642859cec19fa | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 17:29:35 to 01/21/2026 17:33:48 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 762748678 - 2026-01-21 11:31:46 -0600 - 01/21/2026 11:31:46
Added in Camera/UI:
- FFlagRefactorMenuConfirmationButtons4_IXP = 1;UIEcosystem.User.Migration;UIEcosystem.User.Migration.MenuButtonColorRedesign.MemoryFix;62545430;flagbank | Mechanism: Updates the design and functionality of confirmation buttons in menus. | Purpose: Improves user experience by making menu interactions clearer and more intuitive.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 5f22655f856e48a47861f132ad9510fa04664df2 to 537602be5bd36fc9cd31b5d8c7dc97447e867148 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 01:56:34 to 01/21/2026 17:29:35 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 5f22655f856e48a47861f132ad9510fa04664df2 to 537602be5bd36fc9cd31b5d8c7dc97447e867148 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 01:56:34 to 01/21/2026 17:29:35 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## f0932e642 - 2026-01-20 19:57:41 -0600 - 01/20/2026 19:57:41
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 9cb45bc027e13aefc6db1b840eda3a8d3dfe3cbd to 5f22655f856e48a47861f132ad9510fa04664df2 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 01:51:35 to 01/21/2026 01:56:34 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 9cb45bc027e13aefc6db1b840eda3a8d3dfe3cbd to 5f22655f856e48a47861f132ad9510fa04664df2 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 01:51:35 to 01/21/2026 01:56:34 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 357525db4 - 2026-01-20 19:53:10 -0600 - 01/20/2026 19:53:10
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 1974b65763bdfe12d26570abbe1dbfca418dd06d to 9cb45bc027e13aefc6db1b840eda3a8d3dfe3cbd | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 01:41:30 to 01/21/2026 01:51:35 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 1974b65763bdfe12d26570abbe1dbfca418dd06d to 9cb45bc027e13aefc6db1b840eda3a8d3dfe3cbd | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 01:41:30 to 01/21/2026 01:51:35 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 6e9542c1a - 2026-01-20 19:44:15 -0600 - 01/20/2026 19:44:15
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from f4125ba4b9a9e3036c4a3b983e4bad1ea5e84365 to 1974b65763bdfe12d26570abbe1dbfca418dd06d | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 01:36:16 to 01/21/2026 01:41:30 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from f4125ba4b9a9e3036c4a3b983e4bad1ea5e84365 to 1974b65763bdfe12d26570abbe1dbfca418dd06d | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 01:36:16 to 01/21/2026 01:41:30 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## d0ddd85c1 - 2026-01-20 19:37:25 -0600 - 01/20/2026 19:37:25
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 966d84628a2467d016105b2ca32b094922ebf4c6 to f4125ba4b9a9e3036c4a3b983e4bad1ea5e84365 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 01:26:42 to 01/21/2026 01:36:16 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 966d84628a2467d016105b2ca32b094922ebf4c6 to f4125ba4b9a9e3036c4a3b983e4bad1ea5e84365 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 01:26:42 to 01/21/2026 01:36:16 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Changed in Network:
- FFlagWsClientMultiPoll changed from True to False | Mechanism: Enables multiple polling connections for WebSocket clients. | Purpose: Improves real-time data handling and reduces lag during gameplay.
Removed in Network:
- FFlagWsClientMultiPoll_Staged removed (was false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;70592780;2026-01-21T00:32:01) | Mechanism: Tests the multi-polling feature for WebSocket clients in a staged environment. | Purpose: Ensures stability and performance before full rollout to enhance player experience.

## 73c112daa - 2026-01-20 19:28:27 -0600 - 01/20/2026 19:28:27
Changed in Other:
- DFIntPerformanceControlMemoryCriticalBufferSizeMB changed from 200 to 450 | Mechanism: Sets the size limit for critical memory buffers used in performance control. | Purpose: Optimizes game performance by managing memory usage more effectively.
- DFStringFlagRepoGitHashDynamicString changed from dca668487c410532bd34a88476d23b7109f48fbb to 966d84628a2467d016105b2ca32b094922ebf4c6 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 01:25:37 to 01/21/2026 01:26:42 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from dca668487c410532bd34a88476d23b7109f48fbb to 966d84628a2467d016105b2ca32b094922ebf4c6 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 01:25:37 to 01/21/2026 01:26:42 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFIntPerformanceControlMemoryCriticalBufferSizeMB_Staged removed (was 450;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T00:25:00) | Mechanism: Adjusts the amount of memory allocated for critical performance tasks. | Purpose: Optimizes game performance by ensuring enough memory is available for smooth gameplay.

## 987dc5f35 - 2026-01-20 19:26:09 -0600 - 01/20/2026 19:26:09
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from a32e030cff14c5f05f014eceb783fae17e8e6b79 to dca668487c410532bd34a88476d23b7109f48fbb | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 01:06:38 to 01/21/2026 01:25:37 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from a32e030cff14c5f05f014eceb783fae17e8e6b79 to dca668487c410532bd34a88476d23b7109f48fbb | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 01:06:38 to 01/21/2026 01:25:37 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagSimParentPrimSpacePVsWrite2 removed (was True) | Mechanism: Implements an updated method for writing parent-child relationships in the simulation space. | Purpose: Enhances the efficiency and reliability of object interactions in games.
- DFFlagSimParentPrimSpacePVsWrite2_PlaceFilter removed (was true;3633505977) | Mechanism: Enables filtering of place data when writing to parent space properties. | Purpose: Improves performance by ensuring only relevant data is processed for each place.

## c32799829 - 2026-01-20 19:08:13 -0600 - 01/20/2026 19:08:13
Added in Other:
- DFFlagEnableOpenLogsFolderApi = True | Mechanism: Provides an API to open the logs folder directly. | Purpose: Makes it easier for developers to access logs, aiding in troubleshooting and improving game stability.
- FFlagLuaAppIedpFixPlayButton = True | Mechanism: Fixes the functionality of the play button in Lua applications. | Purpose: Ensures players can easily start games without issues.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from fa2f6a32f8bd5b252a7f5e8b731a2bf647342729 to a32e030cff14c5f05f014eceb783fae17e8e6b79 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 00:55:33 to 01/21/2026 01:06:38 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from fa2f6a32f8bd5b252a7f5e8b731a2bf647342729 to a32e030cff14c5f05f014eceb783fae17e8e6b79 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 00:55:33 to 01/21/2026 01:06:38 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagEnableOpenLogsFolderApi_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T23:50:23) | Mechanism: Provides an API to open the logs folder directly. | Purpose: Simplifies access to logs for players, aiding in troubleshooting.
- FFlagLuaAppIedpFixPlayButton_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T23:50:17) | Mechanism: Fixes issues with the play button in the Lua app. | Purpose: Ensures a smoother experience when starting games.

## d5c60d004 - 2026-01-20 18:56:55 -0600 - 01/20/2026 18:56:55
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 2e1fc41220cbbff1156df88583b969807120eca3 to fa2f6a32f8bd5b252a7f5e8b731a2bf647342729 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 00:53:46 to 01/21/2026 00:55:33 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 2e1fc41220cbbff1156df88583b969807120eca3 to fa2f6a32f8bd5b252a7f5e8b731a2bf647342729 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 00:53:46 to 01/21/2026 00:55:33 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## c9cd2e0a4 - 2026-01-20 18:54:37 -0600 - 01/20/2026 18:54:37
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from f674b08050aa79a88c4bfd34688b1712146657f5 to 2e1fc41220cbbff1156df88583b969807120eca3 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 00:47:12 to 01/21/2026 00:53:46 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from f674b08050aa79a88c4bfd34688b1712146657f5 to 2e1fc41220cbbff1156df88583b969807120eca3 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 00:47:12 to 01/21/2026 00:53:46 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## f63783409 - 2026-01-20 18:50:00 -0600 - 01/20/2026 18:50:00
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from d13671f9677af8e178a61da86ea16f84e7d5845f to f674b08050aa79a88c4bfd34688b1712146657f5 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 00:46:52 to 01/21/2026 00:47:12 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from d13671f9677af8e178a61da86ea16f84e7d5845f to f674b08050aa79a88c4bfd34688b1712146657f5 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 00:46:52 to 01/21/2026 00:47:12 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 9c25fa963 - 2026-01-20 18:47:43 -0600 - 01/20/2026 18:47:43
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from ac81d3b02523a8946529b78d3bc2f1449932d6ce to d13671f9677af8e178a61da86ea16f84e7d5845f | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 00:41:52 to 01/21/2026 00:46:52 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from ac81d3b02523a8946529b78d3bc2f1449932d6ce to d13671f9677af8e178a61da86ea16f84e7d5845f | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 00:41:52 to 01/21/2026 00:46:52 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 31b76450c - 2026-01-20 18:43:07 -0600 - 01/20/2026 18:43:07
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from d3b2bfc7cc248eaff6cfda677ad417a8cf59b9a7 to ac81d3b02523a8946529b78d3bc2f1449932d6ce | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 00:39:07 to 01/21/2026 00:41:52 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from d3b2bfc7cc248eaff6cfda677ad417a8cf59b9a7 to ac81d3b02523a8946529b78d3bc2f1449932d6ce | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 00:39:07 to 01/21/2026 00:41:52 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## a4bc7c5ee - 2026-01-20 18:40:49 -0600 - 01/20/2026 18:40:49
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 026fd36c8dfbf7b9dffa34d8ce7e306fc10f669c to d3b2bfc7cc248eaff6cfda677ad417a8cf59b9a7 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 00:37:24 to 01/21/2026 00:39:07 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 026fd36c8dfbf7b9dffa34d8ce7e306fc10f669c to d3b2bfc7cc248eaff6cfda677ad417a8cf59b9a7 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 00:37:24 to 01/21/2026 00:39:07 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## d8d68ac2c - 2026-01-20 18:38:32 -0600 - 01/20/2026 18:38:31
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from c794ec685329e0f5fb42f511a8bc8c93e9ef77b1 to 026fd36c8dfbf7b9dffa34d8ce7e306fc10f669c | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 00:35:35 to 01/21/2026 00:37:24 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from c794ec685329e0f5fb42f511a8bc8c93e9ef77b1 to 026fd36c8dfbf7b9dffa34d8ce7e306fc10f669c | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 00:35:35 to 01/21/2026 00:37:24 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## d5862397b - 2026-01-20 18:36:13 -0600 - 01/20/2026 18:36:13
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from c376e816b67b4979eb57c94614702069ef0f8580 to c794ec685329e0f5fb42f511a8bc8c93e9ef77b1 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 00:33:03 to 01/21/2026 00:35:35 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from c376e816b67b4979eb57c94614702069ef0f8580 to c794ec685329e0f5fb42f511a8bc8c93e9ef77b1 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 00:33:03 to 01/21/2026 00:35:35 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## aa2e60e42 - 2026-01-20 18:33:56 -0600 - 01/20/2026 18:33:56
Added in Camera/UI:
- FFlagShortcutBarFixChatInputCovering = True | Mechanism: Fixes the issue where the chat input overlaps with the shortcut bar. | Purpose: Ensures players can easily use chat without obstruction, improving communication.
Added in Network:
- FFlagWsClientMultiPoll_Staged = false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;70592780;2026-01-21T00:32:01 | Mechanism: Tests the multi-polling feature for WebSocket clients in a staged environment. | Purpose: Ensures stability and performance before full rollout to enhance player experience.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 1da0fbeff54f78eb5da9033870fb0b5722c46e1d to c376e816b67b4979eb57c94614702069ef0f8580 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 00:25:44 to 01/21/2026 00:33:03 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 1da0fbeff54f78eb5da9033870fb0b5722c46e1d to c376e816b67b4979eb57c94614702069ef0f8580 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 00:25:44 to 01/21/2026 00:33:03 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Camera/UI:
- FFlagShortcutBarFixChatInputCovering_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T23:26:54) | Mechanism: Adjusts the layout to prevent the shortcut bar from overlapping the chat input. | Purpose: Improves user experience by ensuring players can see and use the chat without obstruction.

## 7260e66f8 - 2026-01-20 18:27:11 -0600 - 01/20/2026 18:27:11
Added in Other:
- DFIntPerformanceControlMemoryCriticalBufferSizeMB_Staged = 450;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-21T00:25:00 | Mechanism: Adjusts the amount of memory allocated for critical performance tasks. | Purpose: Optimizes game performance by ensuring enough memory is available for smooth gameplay.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 74cead2aae921d73b4299d0a111d37348156afef to 1da0fbeff54f78eb5da9033870fb0b5722c46e1d | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 00:12:13 to 01/21/2026 00:25:44 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 74cead2aae921d73b4299d0a111d37348156afef to 1da0fbeff54f78eb5da9033870fb0b5722c46e1d | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 00:12:13 to 01/21/2026 00:25:44 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## b2a7f262b - 2026-01-20 18:13:47 -0600 - 01/20/2026 18:13:47
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from ecc6712dd351d685971983bce96bb16c202c01da to 74cead2aae921d73b4299d0a111d37348156afef | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/21/2026 00:02:07 to 01/21/2026 00:12:13 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from ecc6712dd351d685971983bce96bb16c202c01da to 74cead2aae921d73b4299d0a111d37348156afef | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/21/2026 00:02:07 to 01/21/2026 00:12:13 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 518d1d9af - 2026-01-20 18:04:47 -0600 - 01/20/2026 18:04:47
Added in Other:
- DFLogBootcampCLI183666Log = Info | Mechanism: Logs specific data related to the bootcamp command line interface. | Purpose: Helps developers troubleshoot and improve the bootcamp experience for new players.
- FFlagBootcampCLI183666 = True | Mechanism: Updates the command line interface for bootcamp tools. | Purpose: Enhances the user experience for new developers learning to create games.
- FFlagMoveLimitedBadgeToTopLeft = True | Mechanism: Changes the position of limited badges on the user interface. | Purpose: Makes it easier for players to see their limited edition items.
- FIntStreamingPauseFlickerStatsThrottleHP = 20 | Mechanism: Controls the throttle rate for flicker stats during streaming pauses. | Purpose: Optimizes performance by managing how often flicker stats are updated.
Added in Graphics:
- FFlagRenderMeshFidelityStats = True | Mechanism: Enables detailed statistics for rendering mesh fidelity in games. | Purpose: Helps developers understand and improve the visual quality of their games.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 8f11af12b532768f6260a9fd321cddf88a0291f8 to ecc6712dd351d685971983bce96bb16c202c01da | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 23:54:07 to 01/21/2026 00:02:07 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FFlagFCColorParametrization changed from True to False | Mechanism: Allows for more flexible color settings in game design. | Purpose: Enables developers to create more visually appealing games with customized colors.
- FStringFlagRepoGitHashFastString changed from 8f11af12b532768f6260a9fd321cddf88a0291f8 to ecc6712dd351d685971983bce96bb16c202c01da | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 23:54:07 to 01/21/2026 00:02:07 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFLogBootcampCLI183666Log_Staged removed (was Info;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:57:06) | Mechanism: Logs specific bootcamp command line interactions. | Purpose: Helps developers track and debug issues during the bootcamp process.
- FFlagAXCatalogCategoriesStore7_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:51:01) | Mechanism: Implements a new way to organize and display catalog categories. | Purpose: Makes it easier for players to find and browse items in the catalog.
- FFlagBootcampCLI183666_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:56:23) | Mechanism: Introduces new command-line interface features for bootcamp tools. | Purpose: Enhances the experience for new developers learning to create games.
- FFlagFCColorParametrization_Staged removed (was false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;56852593;2026-01-20T22:58:16) | Mechanism: Modifies how color parameters are defined and used in the system. | Purpose: Allows for more flexible and accurate color settings in games.
- FFlagMoveLimitedBadgeToTopLeft_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:51:28) | Mechanism: Moves the limited badge display to the top left corner of the screen. | Purpose: Improves visibility of limited badges for players.
- FIntStreamingPauseFlickerStatsThrottleHP_Staged removed (was 20;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:52:32) | Mechanism: Adjusts how frequently the game pauses and resumes streaming data to reduce flickering. | Purpose: Improves the visual experience by minimizing interruptions during gameplay.
Removed in Graphics:
- FFlagRenderMeshFidelityStats_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:41:14) | Mechanism: Tracks and reports the quality of rendered mesh details. | Purpose: Helps developers optimize mesh quality for better visual experiences.

## e08f8d30f - 2026-01-20 17:55:35 -0600 - 01/20/2026 17:55:35
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from e99878636d854caa01e4c02ffd060d0ae4ab157c to 8f11af12b532768f6260a9fd321cddf88a0291f8 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 23:51:55 to 01/20/2026 23:54:07 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from e99878636d854caa01e4c02ffd060d0ae4ab157c to 8f11af12b532768f6260a9fd321cddf88a0291f8 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 23:51:55 to 01/20/2026 23:54:07 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 6c265eeda - 2026-01-20 17:53:17 -0600 - 01/20/2026 17:53:17
Added in Other:
- DFFlagEnableOpenLogsFolderApi_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T23:50:23 | Mechanism: Provides an API to open the logs folder directly. | Purpose: Simplifies access to logs for players, aiding in troubleshooting.
- FFlagLuaAppIedpFixPlayButton_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T23:50:17 | Mechanism: Fixes issues with the play button in the Lua app. | Purpose: Ensures a smoother experience when starting games.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 096cfb0e7ae956bd26bd4cb55511590887f70067 to e99878636d854caa01e4c02ffd060d0ae4ab157c | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 23:50:12 to 01/20/2026 23:51:55 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 096cfb0e7ae956bd26bd4cb55511590887f70067 to e99878636d854caa01e4c02ffd060d0ae4ab157c | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 23:50:12 to 01/20/2026 23:51:55 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## f7b198f5f - 2026-01-20 17:51:00 -0600 - 01/20/2026 17:51:00
Changed in Other:
- DFFlagDataStoreEnableModernRequestCounters_PlaceFilter changed from true;82645084530330;70443751702786;92518825399956 to true;82645084530330;70443751702786;92518825399956;8357232245 | Mechanism: Introduces modern tracking for data requests specific to game places. | Purpose: Allows developers to monitor and optimize data usage for better game performance.
- DFFlagDataStoreEnableModernRequestThrottling_PlaceFilter changed from true;82645084530330;70443751702786;92518825399956 to true;82645084530330;70443751702786;92518825399956;8357232245 | Mechanism: Implements a modern method for limiting data store requests based on place filters. | Purpose: Ensures smoother gameplay by managing data requests more effectively.
- DFIntDataStoreOrderedListFixedRequestLimit_UniverseFilter changed from 500;3666294218 to 500;3666294218;8357232245 | Mechanism: Increases the limit for requests when filtering data in ordered lists. | Purpose: Allows players to access more data at once, enhancing performance in data-heavy games.
- DFIntDataStoreOrderedListPerPlayerRequestLimit_UniverseFilter changed from 10;3666294218 to 10;3666294218;8357232245 | Mechanism: Defines a limit on the number of requests for ordered lists in data stores per player, filtered by universe. | Purpose: Improves game performance by managing how much data can be requested, ensuring smoother gameplay.
- DFIntDataStoreOrderedReadFixedRequestLimit_UniverseFilter changed from 1250;3666294218 to 1250;3666294218;8357232245 | Mechanism: Sets a limit on how many data requests can be made per universe in a fixed order. | Purpose: Improves data management efficiency for developers, ensuring smoother gameplay.
- DFIntDataStoreOrderedReadPerPlayerRequestLimit_UniverseFilter changed from 200;3666294218 to 200;3666294218;8357232245 | Mechanism: Limits the number of data store read requests per player while filtering by universe. | Purpose: Improves performance by reducing server load when accessing player data across different game universes.
- DFIntDataStoreOrderedRemoveFixedRequestLimit_UniverseFilter changed from 500;3666294218 to 500;3666294218;8357232245 | Mechanism: Fixes the request limit for ordered removal operations in data stores with a universe filter. | Purpose: Improves data management capabilities for developers by allowing more efficient data removal.
- DFIntDataStoreOrderedRemovePerPlayerRequestLimit_UniverseFilter changed from 200;3666294218 to 200;3666294218;8357232245 | Mechanism: Limits the number of data removal requests per player in a fixed order. | Purpose: Enhances performance by preventing excessive data removal requests from slowing down the game.
- DFIntDataStoreOrderedWriteFixedRequestLimit_UniverseFilter changed from 1250;3666294218 to 1250;3666294218;8357232245 | Mechanism: Increases the limit for writing requests in ordered data stores. | Purpose: Enables faster saving of player data, reducing wait times and improving gameplay.
- DFIntDataStoreOrderedWritePerPlayerRequestLimit_UniverseFilter changed from 100;3666294218 to 100;3666294218;8357232245 | Mechanism: Sets a limit on how many write requests a player can make to the data store. | Purpose: Prevents abuse of data storage, ensuring fairer gameplay for all players.
- DFIntDataStoreStandardListFixedRequestLimit_UniverseFilter changed from 50;3666294218 to 50;3666294218;8357232245 | Mechanism: Adjusts the request limit for data store operations with a universe filter. | Purpose: Allows developers to manage data more efficiently across different game universes.
- DFIntDataStoreStandardListPerPlayerRequestLimit_UniverseFilter changed from 10;3666294218 to 10;3666294218;8357232245 | Mechanism: Sets a limit on the number of data store requests per player based on universe filtering. | Purpose: Ensures fair usage of data storage, preventing overload and improving game stability for players.
- DFIntDataStoreStandardReadFixedRequestLimit_UniverseFilter changed from 1250;3666294218 to 1250;3666294218;8357232245 | Mechanism: Sets a limit on how many data requests can be made to ensure fair usage across games. | Purpose: Ensures smoother gameplay by preventing data overload and improving performance.
- DFIntDataStoreStandardReadPerPlayerRequestLimit_UniverseFilter changed from 200;3666294218 to 200;3666294218;8357232245 | Mechanism: Sets a limit on data store requests per player based on universe filtering. | Purpose: Optimizes data access for players, ensuring smoother gameplay.
- DFIntDataStoreStandardRemoveFixedRequestLimit_UniverseFilter changed from 500;3666294218 to 500;3666294218;8357232245 | Mechanism: Removes the fixed limit on data store requests for specific universes. | Purpose: Allows developers to save and load more data without hitting request limits, improving game performance.
- DFIntDataStoreStandardRemovePerPlayerRequestLimit_UniverseFilter changed from 200;3666294218 to 200;3666294218;8357232245 | Mechanism: Removes the limit on how many data requests a player can make in a universe. | Purpose: Enables players to access and modify their game data without restrictions, improving gameplay continuity.
- DFIntDataStoreStandardWriteFixedRequestLimit_UniverseFilter changed from 1250;3666294218 to 1250;3666294218;8357232245 | Mechanism: Sets a limit on the number of data store write requests for filtered universes. | Purpose: Ensures fair usage of data storage, preventing overload and improving game stability.
- DFIntDataStoreStandardWritePerPlayerRequestLimit_UniverseFilter changed from 100;3666294218 to 100;3666294218;8357232245 | Mechanism: Changes the limit on how many data requests a player can make to the server. | Purpose: Enhances performance by allowing more efficient data handling for players in a game.
- DFStringFlagRepoGitHashDynamicString changed from 64f90dc1933b5cc124c6f1158b82e4972b1ea9a2 to 096cfb0e7ae956bd26bd4cb55511590887f70067 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 23:42:03 to 01/20/2026 23:50:12 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 64f90dc1933b5cc124c6f1158b82e4972b1ea9a2 to 096cfb0e7ae956bd26bd4cb55511590887f70067 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 23:42:03 to 01/20/2026 23:50:12 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 850dd57c0 - 2026-01-20 17:44:17 -0600 - 01/20/2026 17:44:17
Added in Other:
- FFlagLuaAppAddIgrsRatingToEdp = True | Mechanism: Integrates a rating system for games within the Lua app. | Purpose: Allows players to see ratings for games, helping them choose what to play.
- FFlagStudioUpdatesLinkReleaseNotes = True | Mechanism: Adds a link to release notes for updates in the game development studio. | Purpose: Keeps developers informed about new features and changes in updates.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from e6bb627266a33a76dd05e6b19d0fa678cd85c670 to 64f90dc1933b5cc124c6f1158b82e4972b1ea9a2 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 23:32:42 to 01/20/2026 23:42:03 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FFlagAXMigrateAXFocusBehaviorRoot changed from False to True | Mechanism: Updates the focus behavior for accessibility features in the game. | Purpose: Enhances navigation for players using assistive technologies, making games more accessible.
- FStringFlagRepoGitHashFastString changed from e6bb627266a33a76dd05e6b19d0fa678cd85c670 to 64f90dc1933b5cc124c6f1158b82e4972b1ea9a2 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 23:32:42 to 01/20/2026 23:42:03 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagAXMigrateAXFocusBehaviorRoot_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:40:22) | Mechanism: Updates the focus behavior for accessibility features in the game. | Purpose: Makes games more accessible for players who rely on assistive technologies.
- FFlagLuaAppAddIgrsRatingToEdp_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:38:41) | Mechanism: Integrates in-game rating system into the app for better feedback. | Purpose: Allows players to rate games directly, improving game quality through feedback.
- FFlagStudioUpdatesLinkReleaseNotes_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:37:28) | Mechanism: Adds a link to the release notes in the studio updates section. | Purpose: Helps developers easily find information about new features and changes.

## 73fb6e996 - 2026-01-20 17:35:22 -0600 - 01/20/2026 17:35:22
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from dcf837ae192a8c39d9a49a46bca6e47300d3f459 to e6bb627266a33a76dd05e6b19d0fa678cd85c670 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 23:31:35 to 01/20/2026 23:32:42 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from dcf837ae192a8c39d9a49a46bca6e47300d3f459 to e6bb627266a33a76dd05e6b19d0fa678cd85c670 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 23:31:35 to 01/20/2026 23:32:42 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## cfdeaff45 - 2026-01-20 17:33:05 -0600 - 01/20/2026 17:33:04
Added in Network:
- FFlagWsClientMultiPoll = True | Mechanism: Enables multiple polling connections for WebSocket clients. | Purpose: Improves real-time data handling and reduces lag during gameplay.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from d7fc074b59eb4190fc423c26971583faf779b047 to dcf837ae192a8c39d9a49a46bca6e47300d3f459 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 23:28:17 to 01/20/2026 23:31:35 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from d7fc074b59eb4190fc423c26971583faf779b047 to dcf837ae192a8c39d9a49a46bca6e47300d3f459 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 23:28:17 to 01/20/2026 23:31:35 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
- SFStringRCCChannelName changed from Production to  | Mechanism: N/A (invalid) | Purpose: N/A (invalid)
Removed in Network:
- FFlagWsClientMultiPoll_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;256922603;2026-01-20T22:27:04) | Mechanism: Tests the multi-polling feature for WebSocket clients in a staged environment. | Purpose: Ensures stability and performance before full rollout to enhance player experience.
Removed in Other:
- SFStringRCCChannelName_Staged removed (was ;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:28:16) | Mechanism: N/A (invalid) | Purpose: N/A (invalid)

## ea312c3ed - 2026-01-20 17:30:46 -0600 - 01/20/2026 17:30:46
Added in Camera/UI:
- FFlagShortcutBarFixChatInputCovering_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T23:26:54 | Mechanism: Adjusts the layout to prevent the shortcut bar from overlapping the chat input. | Purpose: Improves user experience by ensuring players can see and use the chat without obstruction.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from b9d6383c5b3a67284f30efbb04346a955fee8644 to d7fc074b59eb4190fc423c26971583faf779b047 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 23:27:15 to 01/20/2026 23:28:17 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from b9d6383c5b3a67284f30efbb04346a955fee8644 to d7fc074b59eb4190fc423c26971583faf779b047 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 23:27:15 to 01/20/2026 23:28:17 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 82fd63b54 - 2026-01-20 17:28:28 -0600 - 01/20/2026 17:28:28
Added in Other:
- FFlagAQCodeExpand = True | Mechanism: Expands the capabilities of the code used for analytics. | Purpose: Provides developers with better tools for understanding player behavior, leading to improved game experiences.
- FFlagInventoryPagesDontUseRawThis = True | Mechanism: Changes how inventory pages are loaded, avoiding direct references. | Purpose: Increases stability and performance of the inventory system for users.
- FFlagStudioUpdateShutdownButtonText = True | Mechanism: Changes the text on the shutdown button in Roblox Studio updates. | Purpose: Provides clearer instructions to users about what will happen when they click the button.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from d9d5166d3d1e837a8da0a085ac19e76853b5360b to b9d6383c5b3a67284f30efbb04346a955fee8644 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 23:21:46 to 01/20/2026 23:27:15 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from d9d5166d3d1e837a8da0a085ac19e76853b5360b to b9d6383c5b3a67284f30efbb04346a955fee8644 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 23:21:46 to 01/20/2026 23:27:15 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagAQCodeExpand_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:24:37) | Mechanism: Enables a staged rollout of expanded code features in the analytics queue. | Purpose: Provides developers with enhanced analytics capabilities to better understand player behavior.
- FFlagInventoryPagesDontUseRawThis_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:23:39) | Mechanism: Changes how inventory pages are processed to avoid using outdated methods. | Purpose: Enhances the inventory experience by making it more efficient and responsive for players.
- FFlagStudioUpdateShutdownButtonText_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;2054416539;2026-01-20T22:21:46) | Mechanism: Changes the text on the shutdown button in the Studio when an update is available. | Purpose: Makes it clearer for developers when they need to restart Studio for updates.

## acd4e6ccb - 2026-01-20 17:23:55 -0600 - 01/20/2026 17:23:55
Added in Other:
- DFFlagSimParentPrimSpacePVsWrite2 = True | Mechanism: Implements an updated method for writing parent-child relationships in the simulation space. | Purpose: Enhances the efficiency and reliability of object interactions in games.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 9ad5d2c7f35a393f4668961c3b83f41101f09a1c to d9d5166d3d1e837a8da0a085ac19e76853b5360b | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 23:07:45 to 01/20/2026 23:21:46 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 9ad5d2c7f35a393f4668961c3b83f41101f09a1c to d9d5166d3d1e837a8da0a085ac19e76853b5360b | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 23:07:45 to 01/20/2026 23:21:46 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagSimParentPrimSpacePVsWrite2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:18:38) | Mechanism: Enables a new way of handling parent-child relationships in the simulation space. | Purpose: Improves performance and accuracy of object positioning in games.

## 799d2b7ce - 2026-01-20 17:10:33 -0600 - 01/20/2026 17:10:33
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from a988aa21d1ecc69ad414dc1c43ccc7b6ae82752a to 9ad5d2c7f35a393f4668961c3b83f41101f09a1c | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 23:07:21 to 01/20/2026 23:07:45 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from a988aa21d1ecc69ad414dc1c43ccc7b6ae82752a to 9ad5d2c7f35a393f4668961c3b83f41101f09a1c | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 23:07:21 to 01/20/2026 23:07:45 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 4d6571774 - 2026-01-20 17:08:16 -0600 - 01/20/2026 17:08:16
Added in Network:
- FFlagFixBytesUsedSendItemsPacket2 = True | Mechanism: Improves the efficiency of data packets sent when players interact with items. | Purpose: Reduces lag and improves item interaction speed for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from deaf4acaa26c7fbf47409fb06c9cf3ae5a21925d to a988aa21d1ecc69ad414dc1c43ccc7b6ae82752a | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 23:02:26 to 01/20/2026 23:07:21 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from deaf4acaa26c7fbf47409fb06c9cf3ae5a21925d to a988aa21d1ecc69ad414dc1c43ccc7b6ae82752a | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 23:02:26 to 01/20/2026 23:07:21 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Network:
- FFlagFixBytesUsedSendItemsPacket2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:01:52) | Mechanism: Adjusts the data size calculation for sending item packets. | Purpose: Improves the efficiency of item transfers, reducing lag when players send or receive items.

## 2275ef862 - 2026-01-20 17:03:45 -0600 - 01/20/2026 17:03:45
Added in Other:
- DFLogBootcampCLI183666Log_Staged = Info;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:57:06 | Mechanism: Logs specific bootcamp command line interactions. | Purpose: Helps developers track and debug issues during the bootcamp process.
- FFlagBootcampCLI183666_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:56:23 | Mechanism: Introduces new command-line interface features for bootcamp tools. | Purpose: Enhances the experience for new developers learning to create games.
- FFlagCoreScriptsProfilerDeviceTier = True | Mechanism: Enables profiling of core scripts based on the device tier. | Purpose: Helps developers optimize their games for different devices, enhancing player experience.
- FFlagCoreScriptsProfilerTelemetryContext = True | Mechanism: Adds telemetry data for core scripts to monitor performance. | Purpose: Helps developers identify and fix performance issues in their games.
- FFlagFCColorParametrization_Staged = false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;56852593;2026-01-20T22:58:16 | Mechanism: Modifies how color parameters are defined and used in the system. | Purpose: Allows for more flexible and accurate color settings in games.
- FFlagTelemetryExposeFlushFunction = True | Mechanism: Allows the telemetry system to clear or 'flush' data more effectively. | Purpose: Enhances performance monitoring and data collection for better game insights.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from a5189b64fb0ac09b1b50023839f3157e53414a3a to deaf4acaa26c7fbf47409fb06c9cf3ae5a21925d | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 22:57:25 to 01/20/2026 23:02:26 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from a5189b64fb0ac09b1b50023839f3157e53414a3a to deaf4acaa26c7fbf47409fb06c9cf3ae5a21925d | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 22:57:25 to 01/20/2026 23:02:26 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagCoreScriptsProfilerDeviceTier_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;1216218056;2026-01-20T21:51:43) | Mechanism: Enables profiling of core scripts based on device performance tiers. | Purpose: Helps improve game performance by optimizing scripts for different devices.
- FFlagCoreScriptsProfilerTelemetryContext_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;1216218056;2026-01-20T21:51:43) | Mechanism: Enhances telemetry data collection for core scripts performance profiling. | Purpose: Helps developers understand script performance better, leading to smoother games.
- FFlagTelemetryExposeFlushFunction_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T21:51:25) | Mechanism: Exposes a function to clear telemetry data more effectively. | Purpose: Improves data management for developers, leading to better game stability and performance for players.

## 0a6a1dedd - 2026-01-20 16:59:10 -0600 - 01/20/2026 16:59:10
Added in Other:
- FFlagMoveLimitedBadgeToTopLeft_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:51:28 | Mechanism: Moves the limited badge display to the top left corner of the screen. | Purpose: Improves visibility of limited badges for players.
- FIntStreamingPauseFlickerStatsThrottleHP_Staged = 20;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:52:32 | Mechanism: Adjusts how frequently the game pauses and resumes streaming data to reduce flickering. | Purpose: Improves the visual experience by minimizing interruptions during gameplay.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from f861237b4a08a6969eabc81840fe09a614a19b6c to a5189b64fb0ac09b1b50023839f3157e53414a3a | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 22:56:06 to 01/20/2026 22:57:25 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from f861237b4a08a6969eabc81840fe09a614a19b6c to a5189b64fb0ac09b1b50023839f3157e53414a3a | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 22:56:06 to 01/20/2026 22:57:25 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 44c79901d - 2026-01-20 16:56:53 -0600 - 01/20/2026 16:56:52
Added in Other:
- FFlagAXCatalogCategoriesStore7_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:51:01 | Mechanism: Implements a new way to organize and display catalog categories. | Purpose: Makes it easier for players to find and browse items in the catalog.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from b2e342e7740431f8494768b52308f558e5a9469a to f861237b4a08a6969eabc81840fe09a614a19b6c | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 22:45:37 to 01/20/2026 22:56:06 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from b2e342e7740431f8494768b52308f558e5a9469a to f861237b4a08a6969eabc81840fe09a614a19b6c | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 22:45:37 to 01/20/2026 22:56:06 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 1052f927d - 2026-01-20 16:47:52 -0600 - 01/20/2026 16:47:52
Added in Graphics:
- FFlagRenderMeshFidelityStats_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:41:14 | Mechanism: Tracks and reports the quality of rendered mesh details. | Purpose: Helps developers optimize mesh quality for better visual experiences.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from c0f5511c113d3b06eb535fd9fd20ff85fb89df15 to b2e342e7740431f8494768b52308f558e5a9469a | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 22:44:40 to 01/20/2026 22:45:37 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from c0f5511c113d3b06eb535fd9fd20ff85fb89df15 to b2e342e7740431f8494768b52308f558e5a9469a | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 22:44:40 to 01/20/2026 22:45:37 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 12706c634 - 2026-01-20 16:45:34 -0600 - 01/20/2026 16:45:34
Added in Other:
- FFlagAXMigrateAXFocusBehaviorRoot_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:40:22 | Mechanism: Updates the focus behavior for accessibility features in the game. | Purpose: Makes games more accessible for players who rely on assistive technologies.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from cb1435c298240ef0e7f8a20defda5cae88e3f613 to c0f5511c113d3b06eb535fd9fd20ff85fb89df15 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 22:40:06 to 01/20/2026 22:44:40 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from cb1435c298240ef0e7f8a20defda5cae88e3f613 to c0f5511c113d3b06eb535fd9fd20ff85fb89df15 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 22:40:06 to 01/20/2026 22:44:40 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 439886161 - 2026-01-20 16:41:00 -0600 - 01/20/2026 16:41:00
Added in Other:
- FFlagLuaAppAddIgrsRatingToEdp_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:38:41 | Mechanism: Integrates in-game rating system into the app for better feedback. | Purpose: Allows players to rate games directly, improving game quality through feedback.
- FFlagStudioUpdatesLinkReleaseNotes_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:37:28 | Mechanism: Adds a link to the release notes in the studio updates section. | Purpose: Helps developers easily find information about new features and changes.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from f12cddc0e2bc0cd471a4b8112224b2c2c94c87fb to cb1435c298240ef0e7f8a20defda5cae88e3f613 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 22:37:16 to 01/20/2026 22:40:06 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from f12cddc0e2bc0cd471a4b8112224b2c2c94c87fb to cb1435c298240ef0e7f8a20defda5cae88e3f613 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 22:37:16 to 01/20/2026 22:40:06 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 5bd824652 - 2026-01-20 16:38:42 -0600 - 01/20/2026 16:38:42
Added in Other:
- DFFlagMigrateTriangleMeshPart7041 = True | Mechanism: Migrates triangle mesh parts to a new system for better performance. | Purpose: Enhances the rendering of 3D models, making them look smoother.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from ab08844ee53bd36aff9e6bf0f2f767b25a886970 to f12cddc0e2bc0cd471a4b8112224b2c2c94c87fb | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 22:31:30 to 01/20/2026 22:37:16 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from ab08844ee53bd36aff9e6bf0f2f767b25a886970 to f12cddc0e2bc0cd471a4b8112224b2c2c94c87fb | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 22:31:30 to 01/20/2026 22:37:16 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagMigrateTriangleMeshPart7041_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;false;1125896752;2026-01-20T21:34:17) | Mechanism: Phases the migration of triangle mesh parts to improve stability. | Purpose: Gradually improves game performance while minimizing disruptions.

## 343168e4d - 2026-01-20 16:34:13 -0600 - 01/20/2026 16:34:13
Added in Other:
- FFlagRemoteAllowListExtraTelemetry = True | Mechanism: Enables additional telemetry data collection for remote function calls. | Purpose: Helps developers understand how players interact with remote functions, leading to better game features.
- FFlagVisiblePasswordIsText = True | Mechanism: Allows passwords to be displayed as plain text instead of dots. | Purpose: Helps players confirm their password entries easily.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 84e8c9a7f54114ec52a81f942431bb3145b5f20c to ab08844ee53bd36aff9e6bf0f2f767b25a886970 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 22:29:28 to 01/20/2026 22:31:30 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FFlagAdjustAudioLoaderThreadCount changed from True to False | Mechanism: Changes the number of threads used to load audio files. | Purpose: Improves audio loading speed and performance in games.
- FStringFlagRepoGitHashFastString changed from 84e8c9a7f54114ec52a81f942431bb3145b5f20c to ab08844ee53bd36aff9e6bf0f2f767b25a886970 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 22:29:28 to 01/20/2026 22:31:30 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagAdjustAudioLoaderThreadCount_Staged removed (was false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T21:25:48) | Mechanism: Adjusts the number of threads used for loading audio assets. | Purpose: Improves audio loading times, leading to a better overall gameplay experience.
- FFlagRemoteAllowListExtraTelemetry_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T21:26:25) | Mechanism: Adds more telemetry data for remote function calls. | Purpose: Enhances performance monitoring for developers, leading to smoother gameplay for players.
- FFlagVisiblePasswordIsText_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T21:25:22) | Mechanism: Changes password visibility from dots to plain text when requested. | Purpose: Helps players confirm their passwords more easily when logging in.

## f8a99f11b - 2026-01-20 16:31:56 -0600 - 01/20/2026 16:31:56
Added in Other:
- SFStringRCCChannelName_Staged = ;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:28:16 | Mechanism: N/A (invalid) | Purpose: N/A (invalid)
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 50af4cb8f0f92e67bfc0599bd8ec4714ce6a1ae0 to 84e8c9a7f54114ec52a81f942431bb3145b5f20c | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 22:29:05 to 01/20/2026 22:29:28 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 50af4cb8f0f92e67bfc0599bd8ec4714ce6a1ae0 to 84e8c9a7f54114ec52a81f942431bb3145b5f20c | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 22:29:05 to 01/20/2026 22:29:28 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## c1f7ad8ac - 2026-01-20 16:29:38 -0600 - 01/20/2026 16:29:38
Added in Other:
- DFFlagMigrateTriangleMeshPartSkipDM = True | Mechanism: Updates how triangle mesh parts are processed, skipping certain steps. | Purpose: Increases performance and reduces loading times for complex models.
- FFlagFoundationAnimateTabs2 = True | Mechanism: Introduces enhanced animations for tab transitions in the UI. | Purpose: Makes the user interface feel smoother and more engaging when switching between tabs.
Added in Network:
- FFlagWsClientMultiPoll_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;256922603;2026-01-20T22:27:04 | Mechanism: Tests the multi-polling feature for WebSocket clients in a staged environment. | Purpose: Ensures stability and performance before full rollout to enhance player experience.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from a8a3fa9cbc943967e09a6ca1fbd3706040a978af to 50af4cb8f0f92e67bfc0599bd8ec4714ce6a1ae0 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 22:25:25 to 01/20/2026 22:29:05 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from a8a3fa9cbc943967e09a6ca1fbd3706040a978af to 50af4cb8f0f92e67bfc0599bd8ec4714ce6a1ae0 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 22:25:25 to 01/20/2026 22:29:05 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Changed in Camera/UI:
- FIntRelocateMobileMenuButtonsVariant_IXP changed from 1;UIEcosystem.User.Migration;IxpFlagLink;398703262;flagbank to 1;UIEcosystem.User.Migration;UIEcosystem.User.Migration.ReactPeoplePageAndCardLayout2;398703262;flagbank | Mechanism: Moves buttons in the mobile menu to a new layout. | Purpose: Improves navigation and accessibility for mobile players.
Removed in Other:
- DFFlagMigrateTriangleMeshPartSkipDM_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;false;1132657652;2026-01-20T21:23:01) | Mechanism: Skips certain data migration processes for triangle mesh parts. | Purpose: Enhances performance by reducing load times for games using triangle mesh parts.
- FFlagFoundationAnimateTabs2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;1574265837;2026-01-20T21:20:08) | Mechanism: Introduces a new way to manage animation tabs in the development interface. | Purpose: Makes it easier for developers to organize and access their animations.

## c4bfd75d6 - 2026-01-20 16:27:20 -0600 - 01/20/2026 16:27:19
Added in Other:
- FFlagAQCodeExpand_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:24:37 | Mechanism: Enables a staged rollout of expanded code features in the analytics queue. | Purpose: Provides developers with enhanced analytics capabilities to better understand player behavior.
- FFlagInventoryPagesDontUseRawThis_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:23:39 | Mechanism: Changes how inventory pages are processed to avoid using outdated methods. | Purpose: Enhances the inventory experience by making it more efficient and responsive for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 4874eb1a87a06c8c5b13c59e06461ff9a98dbbca to a8a3fa9cbc943967e09a6ca1fbd3706040a978af | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 22:23:07 to 01/20/2026 22:25:25 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 4874eb1a87a06c8c5b13c59e06461ff9a98dbbca to a8a3fa9cbc943967e09a6ca1fbd3706040a978af | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 22:23:07 to 01/20/2026 22:25:25 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 6cb260771 - 2026-01-20 16:25:02 -0600 - 01/20/2026 16:25:02
Added in Other:
- FFlagStudioUpdateShutdownButtonText_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;2054416539;2026-01-20T22:21:46 | Mechanism: Changes the text on the shutdown button in the Studio when an update is available. | Purpose: Makes it clearer for developers when they need to restart Studio for updates.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from d1c1eb27fc37ad2b22517cefb22401437acd1e4e to 4874eb1a87a06c8c5b13c59e06461ff9a98dbbca | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 22:21:43 to 01/20/2026 22:23:07 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from d1c1eb27fc37ad2b22517cefb22401437acd1e4e to 4874eb1a87a06c8c5b13c59e06461ff9a98dbbca | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 22:21:43 to 01/20/2026 22:23:07 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 8288152f6 - 2026-01-20 16:22:44 -0600 - 01/20/2026 16:22:44
Added in Other:
- DFFlagSecurityCapabilitiesNewToString = True | Mechanism: Updates the way security capabilities are converted to string format. | Purpose: Enhances clarity and usability of security information for developers.
- DFFlagSimParentPrimSpacePVsWrite2_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:18:38 | Mechanism: Enables a new way of handling parent-child relationships in the simulation space. | Purpose: Improves performance and accuracy of object positioning in games.
- FFlagFoundationAnimateSegmentedControl = True | Mechanism: Introduces animations for segmented control elements in the UI. | Purpose: Provides a more visually appealing and interactive experience for users when navigating options.
- FFlagFoundationRemoveDividerSegmentedControl = True | Mechanism: Removes a visual divider in segmented controls. | Purpose: Simplifies the user interface for a cleaner look and easier interaction.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from df78084f6bbd19d6aaa47384ea3e64556aa5323f to d1c1eb27fc37ad2b22517cefb22401437acd1e4e | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 22:18:44 to 01/20/2026 22:21:43 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from df78084f6bbd19d6aaa47384ea3e64556aa5323f to d1c1eb27fc37ad2b22517cefb22401437acd1e4e | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 22:18:44 to 01/20/2026 22:21:43 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagSecurityCapabilitiesNewToString_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T21:15:31) | Mechanism: Introduces new security features for converting objects to strings safely. | Purpose: Enhances security when handling object data, making the game safer for players.
- FFlagFoundationAnimateSegmentedControl_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;623615220;2026-01-20T21:19:19) | Mechanism: Adds animations to segmented control elements in the UI. | Purpose: Provides a smoother and more engaging user interface experience for players.
- FFlagFoundationRemoveDividerSegmentedControl_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;623615220;2026-01-20T21:19:19) | Mechanism: Removes visual dividers in segmented controls for a cleaner interface. | Purpose: Creates a more streamlined and user-friendly experience for players when navigating options.

## c926671d8 - 2026-01-20 16:20:27 -0600 - 01/20/2026 16:20:27
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 00ca219597db571194b254a6433872c3badd536a to df78084f6bbd19d6aaa47384ea3e64556aa5323f | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 22:16:40 to 01/20/2026 22:18:44 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 00ca219597db571194b254a6433872c3badd536a to df78084f6bbd19d6aaa47384ea3e64556aa5323f | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 22:16:40 to 01/20/2026 22:18:44 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## b4b14729b - 2026-01-20 16:18:09 -0600 - 01/20/2026 16:18:09
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from e9b15b008bb4282a1d6841d4354a34d597ae12b5 to 00ca219597db571194b254a6433872c3badd536a | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 22:11:31 to 01/20/2026 22:16:40 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from e9b15b008bb4282a1d6841d4354a34d597ae12b5 to 00ca219597db571194b254a6433872c3badd536a | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 22:11:31 to 01/20/2026 22:16:40 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 54b9e12eb - 2026-01-20 16:13:38 -0600 - 01/20/2026 16:13:38
Added in Other:
- FFlagAXCatalogSearchParamTypes = True | Mechanism: Enables different types of search parameters in the catalog. | Purpose: Improves the search experience for players by allowing more specific searches for items.
Added in Input:
- FFlagRefreshRbxKeyboardAutofill2 = True | Mechanism: Updates the keyboard autofill feature for user inputs. | Purpose: Makes it easier for players to enter information quickly and accurately.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from cc5575131874fc123624523b52eee5719150ace1 to e9b15b008bb4282a1d6841d4354a34d597ae12b5 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 22:07:16 to 01/20/2026 22:11:31 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from cc5575131874fc123624523b52eee5719150ace1 to e9b15b008bb4282a1d6841d4354a34d597ae12b5 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 22:07:16 to 01/20/2026 22:11:31 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagAXCatalogSearchParamTypes_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T21:09:04) | Mechanism: Introduces new search parameters for the catalog search feature. | Purpose: Players can find items more easily and accurately in the catalog.
Removed in Input:
- FFlagRefreshRbxKeyboardAutofill2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T21:05:45) | Mechanism: Implements an updated autofill feature for the Roblox keyboard. | Purpose: Improves the typing experience by suggesting words and phrases faster.

## 005636f1e - 2026-01-20 16:09:08 -0600 - 01/20/2026 16:09:07
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 56148262670f9d83222a0e96e38dccdc557ded61 to cc5575131874fc123624523b52eee5719150ace1 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 22:02:41 to 01/20/2026 22:07:16 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 56148262670f9d83222a0e96e38dccdc557ded61 to cc5575131874fc123624523b52eee5719150ace1 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 22:02:41 to 01/20/2026 22:07:16 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagSimParentPrimSpacePVsWrite2_Staged removed (was true;SteadyState;10;30;Revert;2026-01-20T21:34:14) | Mechanism: Enables a new way of handling parent-child relationships in the simulation space. | Purpose: Improves performance and accuracy of object positioning in games.

## b7233e603 - 2026-01-20 16:04:37 -0600 - 01/20/2026 16:04:36
Added in Network:
- FFlagFixBytesUsedSendItemsPacket2_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T22:01:52 | Mechanism: Adjusts the data size calculation for sending item packets. | Purpose: Improves the efficiency of item transfers, reducing lag when players send or receive items.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from a151c1049cfe0ed137807c985da3daf581aeb510 to 56148262670f9d83222a0e96e38dccdc557ded61 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 21:53:35 to 01/20/2026 22:02:41 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from a151c1049cfe0ed137807c985da3daf581aeb510 to 56148262670f9d83222a0e96e38dccdc557ded61 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 21:53:35 to 01/20/2026 22:02:41 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagIkControlFixSetup_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T20:56:06) | Mechanism: Fixes the setup process for inverse kinematics controls in animations. | Purpose: Ensures smoother and more accurate character movements for players.

## a6123fd23 - 2026-01-20 16:02:19 -0600 - 01/20/2026 16:02:19
Added in Other:
- DFFlagIkControlFixSetup = True | Mechanism: Fixes the setup for inverse kinematics controls in animations. | Purpose: Provides smoother and more accurate character animations.

## d5d18933c - 2026-01-20 15:55:34 -0600 - 01/20/2026 15:55:34
Added in Other:
- FFlagCoreScriptsProfilerDeviceTier_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;1216218056;2026-01-20T21:51:43 | Mechanism: Enables profiling of core scripts based on device performance tiers. | Purpose: Helps improve game performance by optimizing scripts for different devices.
- FFlagCoreScriptsProfilerTelemetryContext_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;1216218056;2026-01-20T21:51:43 | Mechanism: Enhances telemetry data collection for core scripts performance profiling. | Purpose: Helps developers understand script performance better, leading to smoother games.
- FFlagTelemetryExposeFlushFunction_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T21:51:25 | Mechanism: Exposes a function to clear telemetry data more effectively. | Purpose: Improves data management for developers, leading to better game stability and performance for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from ee87b5b7066708423e77467896c8ecb9721e7d13 to a151c1049cfe0ed137807c985da3daf581aeb510 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 21:50:37 to 01/20/2026 21:53:35 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from ee87b5b7066708423e77467896c8ecb9721e7d13 to a151c1049cfe0ed137807c985da3daf581aeb510 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 21:50:37 to 01/20/2026 21:53:35 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 0ed8fcf00 - 2026-01-20 15:53:16 -0600 - 01/20/2026 15:53:16
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 8bfb0c2b0255fa7ac4a742fb2d92de56ada0ce8d to ee87b5b7066708423e77467896c8ecb9721e7d13 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 21:49:34 to 01/20/2026 21:50:37 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 8bfb0c2b0255fa7ac4a742fb2d92de56ada0ce8d to ee87b5b7066708423e77467896c8ecb9721e7d13 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 21:49:34 to 01/20/2026 21:50:37 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagHttpCacheAllowEmptyUrlInAssetCacheHeaders_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T21:48:36) | Mechanism: Allows caching of assets even if the URL is empty in certain headers. | Purpose: Improves loading times for players by enabling better asset caching.

## 35f52825e - 2026-01-20 15:50:58 -0600 - 01/20/2026 15:50:58
Added in Other:
- DFFlagHttpCacheAllowEmptyUrlInAssetCacheHeaders_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T21:48:36 | Mechanism: Allows caching of assets even if the URL is empty in certain headers. | Purpose: Improves loading times for players by enabling better asset caching.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 8acdc30b2728a9a81d7e8d185e9601a7130ed1a2 to 8bfb0c2b0255fa7ac4a742fb2d92de56ada0ce8d | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 21:46:55 to 01/20/2026 21:49:34 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 8acdc30b2728a9a81d7e8d185e9601a7130ed1a2 to 8bfb0c2b0255fa7ac4a742fb2d92de56ada0ce8d | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 21:46:55 to 01/20/2026 21:49:34 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 94c3a5898 - 2026-01-20 15:48:40 -0600 - 01/20/2026 15:48:40
Added in Other:
- DFFlagReflectionServiceFixRootCrash = True | Mechanism: Addresses crashes related to the reflection service in the game engine. | Purpose: Reduces unexpected game crashes, providing a more stable gaming experience.
- FFlagLogRewardedVideoDevProductId = True | Mechanism: Logs the developer product ID when a rewarded video is watched. | Purpose: Helps developers track which products are being rewarded, enhancing monetization strategies.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 7fb6d2b1f201807486ee799f12e742d96e278e51 to 8acdc30b2728a9a81d7e8d185e9601a7130ed1a2 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 21:36:32 to 01/20/2026 21:46:55 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 7fb6d2b1f201807486ee799f12e742d96e278e51 to 8acdc30b2728a9a81d7e8d185e9601a7130ed1a2 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 21:36:32 to 01/20/2026 21:46:55 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagReflectionServiceFixRootCrash_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T20:38:55) | Mechanism: Fixes a bug in the reflection service that caused crashes. | Purpose: Enhances game stability by preventing crashes related to the reflection service.
- FFlagLogRewardedVideoDevProductId_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T20:44:08) | Mechanism: Logs the developer product ID when a rewarded video ad is shown. | Purpose: Provides developers with better analytics on ad performance, helping them optimize monetization strategies.

## d7e1440e1 - 2026-01-20 15:37:27 -0600 - 01/20/2026 15:37:27
Added in Other:
- DFFlagMigrateTriangleMeshPart7041_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;false;1125896752;2026-01-20T21:34:17 | Mechanism: Phases the migration of triangle mesh parts to improve stability. | Purpose: Gradually improves game performance while minimizing disruptions.
- DFFlagSimParentPrimSpacePVsWrite2_Staged = true;SteadyState;10;30;Revert;2026-01-20T21:34:14 | Mechanism: Enables a new way of handling parent-child relationships in the simulation space. | Purpose: Improves performance and accuracy of object positioning in games.
Added in Camera/UI:
- DFFlagSerializerReadBoolsAsUInts = True | Mechanism: Changes how boolean values are read by converting them to unsigned integers. | Purpose: Improves data handling efficiency and reduces errors in data processing.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from f4ad51aa4c8458af8b05baadb2c74aba93803f75 to 7fb6d2b1f201807486ee799f12e742d96e278e51 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 21:28:40 to 01/20/2026 21:36:32 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from f4ad51aa4c8458af8b05baadb2c74aba93803f75 to 7fb6d2b1f201807486ee799f12e742d96e278e51 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 21:28:40 to 01/20/2026 21:36:32 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Camera/UI:
- DFFlagSerializerReadBoolsAsUInts_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T20:33:47) | Mechanism: Changes how boolean values are read, treating them as unsigned integers. | Purpose: Improves data handling efficiency, leading to smoother gameplay experiences.

## 9522bf9c2 - 2026-01-20 15:30:38 -0600 - 01/20/2026 15:30:37
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 636368fbfb1eb11e18cbc1ce856782520e9359a5 to f4ad51aa4c8458af8b05baadb2c74aba93803f75 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 21:27:22 to 01/20/2026 21:28:40 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 636368fbfb1eb11e18cbc1ce856782520e9359a5 to f4ad51aa4c8458af8b05baadb2c74aba93803f75 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 21:27:22 to 01/20/2026 21:28:40 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 12c335806 - 2026-01-20 15:28:18 -0600 - 01/20/2026 15:28:17
Added in Other:
- FFlagAdjustAudioLoaderThreadCount_Staged = false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T21:25:48 | Mechanism: Adjusts the number of threads used for loading audio assets. | Purpose: Improves audio loading times, leading to a better overall gameplay experience.
- FFlagRemoteAllowListExtraTelemetry_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T21:26:25 | Mechanism: Adds more telemetry data for remote function calls. | Purpose: Enhances performance monitoring for developers, leading to smoother gameplay for players.
- FFlagVisiblePasswordIsText_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T21:25:22 | Mechanism: Changes password visibility from dots to plain text when requested. | Purpose: Helps players confirm their passwords more easily when logging in.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from bcee839198750bf0aee765d78b2a272b729e472b to 636368fbfb1eb11e18cbc1ce856782520e9359a5 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 21:24:04 to 01/20/2026 21:27:22 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from bcee839198750bf0aee765d78b2a272b729e472b to 636368fbfb1eb11e18cbc1ce856782520e9359a5 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 21:24:04 to 01/20/2026 21:27:22 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## f4899e322 - 2026-01-20 15:25:58 -0600 - 01/20/2026 15:25:58
Added in Other:
- DFFlagMigrateTriangleMeshPartSkipDM_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;false;1132657652;2026-01-20T21:23:01 | Mechanism: Skips certain data migration processes for triangle mesh parts. | Purpose: Enhances performance by reducing load times for games using triangle mesh parts.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 0406d9fcf91ed1918eeecb546cedee9e677b49fe to bcee839198750bf0aee765d78b2a272b729e472b | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 21:21:30 to 01/20/2026 21:24:04 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 0406d9fcf91ed1918eeecb546cedee9e677b49fe to bcee839198750bf0aee765d78b2a272b729e472b | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 21:21:30 to 01/20/2026 21:24:04 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 149028317 - 2026-01-20 15:23:40 -0600 - 01/20/2026 15:23:40
Added in Other:
- FFlagFoundationAnimateTabs2_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;1574265837;2026-01-20T21:20:08 | Mechanism: Introduces a new way to manage animation tabs in the development interface. | Purpose: Makes it easier for developers to organize and access their animations.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 71403f0d51d075634d265ee894afd2e76ce39d94 to 0406d9fcf91ed1918eeecb546cedee9e677b49fe | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 21:20:13 to 01/20/2026 21:21:30 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 71403f0d51d075634d265ee894afd2e76ce39d94 to 0406d9fcf91ed1918eeecb546cedee9e677b49fe | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 21:20:13 to 01/20/2026 21:21:30 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## ef06eed66 - 2026-01-20 15:21:22 -0600 - 01/20/2026 15:21:22
Added in Other:
- FFlagFoundationAnimateSegmentedControl_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;623615220;2026-01-20T21:19:19 | Mechanism: Adds animations to segmented control elements in the UI. | Purpose: Provides a smoother and more engaging user interface experience for players.
- FFlagFoundationRemoveDividerSegmentedControl_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;true;623615220;2026-01-20T21:19:19 | Mechanism: Removes visual dividers in segmented controls for a cleaner interface. | Purpose: Creates a more streamlined and user-friendly experience for players when navigating options.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 8682f3d51a3416e012f3f37774d7b96575f5fb9f to 71403f0d51d075634d265ee894afd2e76ce39d94 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 21:16:19 to 01/20/2026 21:20:13 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 8682f3d51a3416e012f3f37774d7b96575f5fb9f to 71403f0d51d075634d265ee894afd2e76ce39d94 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 21:16:19 to 01/20/2026 21:20:13 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 995bf7316 - 2026-01-20 15:19:03 -0600 - 01/20/2026 15:19:03
Added in Other:
- DFFlagSecurityCapabilitiesNewToString_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T21:15:31 | Mechanism: Introduces new security features for converting objects to strings safely. | Purpose: Enhances security when handling object data, making the game safer for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from b4f0f9f0f39d98a530583cd79420848a807ac10c to 8682f3d51a3416e012f3f37774d7b96575f5fb9f | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 21:14:43 to 01/20/2026 21:16:19 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from b4f0f9f0f39d98a530583cd79420848a807ac10c to 8682f3d51a3416e012f3f37774d7b96575f5fb9f | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 21:14:43 to 01/20/2026 21:16:19 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 7a8e31aa1 - 2026-01-20 15:16:47 -0600 - 01/20/2026 15:16:47
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from c6220572229b79a1ba0e15aa0ef5d15e1ea21082 to b4f0f9f0f39d98a530583cd79420848a807ac10c | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 21:10:20 to 01/20/2026 21:14:43 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from c6220572229b79a1ba0e15aa0ef5d15e1ea21082 to b4f0f9f0f39d98a530583cd79420848a807ac10c | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 21:10:20 to 01/20/2026 21:14:43 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## f61fc6b29 - 2026-01-20 15:12:15 -0600 - 01/20/2026 15:12:15
Added in Other:
- FFlagAXCatalogSearchParamTypes_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T21:09:04 | Mechanism: Introduces new search parameters for the catalog search feature. | Purpose: Players can find items more easily and accurately in the catalog.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 70144054bd1dfffe182fd315ee07c57cb8932457 to c6220572229b79a1ba0e15aa0ef5d15e1ea21082 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 21:07:58 to 01/20/2026 21:10:20 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 70144054bd1dfffe182fd315ee07c57cb8932457 to c6220572229b79a1ba0e15aa0ef5d15e1ea21082 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 21:07:58 to 01/20/2026 21:10:20 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 88f3f44e6 - 2026-01-20 15:09:57 -0600 - 01/20/2026 15:09:57
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 29888bb3c6a9e1e72a8a74e07215896ad7c320f4 to 70144054bd1dfffe182fd315ee07c57cb8932457 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 21:06:32 to 01/20/2026 21:07:58 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 29888bb3c6a9e1e72a8a74e07215896ad7c320f4 to 70144054bd1dfffe182fd315ee07c57cb8932457 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 21:06:32 to 01/20/2026 21:07:58 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## a85699bec - 2026-01-20 15:07:38 -0600 - 01/20/2026 15:07:38
Added in Input:
- FFlagRefreshRbxKeyboardAutofill2_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T21:05:45 | Mechanism: Implements an updated autofill feature for the Roblox keyboard. | Purpose: Improves the typing experience by suggesting words and phrases faster.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from a221eb6c6fb8e62c403b9f5c8f26fe742f234d32 to 29888bb3c6a9e1e72a8a74e07215896ad7c320f4 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 21:01:45 to 01/20/2026 21:06:32 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from a221eb6c6fb8e62c403b9f5c8f26fe742f234d32 to 29888bb3c6a9e1e72a8a74e07215896ad7c320f4 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 21:01:45 to 01/20/2026 21:06:32 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## f4f48e228 - 2026-01-20 15:03:05 -0600 - 01/20/2026 15:03:05
Added in Other:
- DFIntTriangleMeshPartMigrationPerDMScale = 100000 | Mechanism: Adjusts how triangle mesh parts are scaled in the game engine. | Purpose: Improves the visual quality and performance of 3D models.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from b8f82b158382af31410871b7a412b21c9a5a7e81 to a221eb6c6fb8e62c403b9f5c8f26fe742f234d32 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 20:57:05 to 01/20/2026 21:01:45 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from b8f82b158382af31410871b7a412b21c9a5a7e81 to a221eb6c6fb8e62c403b9f5c8f26fe742f234d32 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 20:57:05 to 01/20/2026 21:01:45 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFIntTriangleMeshPartMigrationPerDMScale_Staged removed (was 100000;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;false;1243995815;2026-01-20T19:59:53) | Mechanism: Migrates triangle mesh parts to a new system based on dynamic scaling. | Purpose: Improves the performance and appearance of 3D models in games.

## 8c0e01018 - 2026-01-20 14:58:32 -0600 - 01/20/2026 14:58:32
Added in Other:
- DFFlagIkControlFixSetup_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T20:56:06 | Mechanism: Fixes the setup process for inverse kinematics controls in animations. | Purpose: Ensures smoother and more accurate character movements for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 0516597a8b24f98da53b35e7a99d7c5b18a331c6 to b8f82b158382af31410871b7a412b21c9a5a7e81 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 20:51:15 to 01/20/2026 20:57:05 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 0516597a8b24f98da53b35e7a99d7c5b18a331c6 to b8f82b158382af31410871b7a412b21c9a5a7e81 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 20:51:15 to 01/20/2026 20:57:05 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 16b077f94 - 2026-01-20 14:54:01 -0600 - 01/20/2026 14:54:00
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from aaa5879ec174c2d6322106280c816943b9e4f015 to 0516597a8b24f98da53b35e7a99d7c5b18a331c6 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 20:44:57 to 01/20/2026 20:51:15 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from aaa5879ec174c2d6322106280c816943b9e4f015 to 0516597a8b24f98da53b35e7a99d7c5b18a331c6 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 20:44:57 to 01/20/2026 20:51:15 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 4267425a0 - 2026-01-20 14:47:14 -0600 - 01/20/2026 14:47:14
Added in Other:
- FFlagLogRewardedVideoDevProductId_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T20:44:08 | Mechanism: Logs the developer product ID when a rewarded video ad is shown. | Purpose: Provides developers with better analytics on ad performance, helping them optimize monetization strategies.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 7fc51b00d39ad67002fcbd46c6f67431a8944ac0 to aaa5879ec174c2d6322106280c816943b9e4f015 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 20:41:31 to 01/20/2026 20:44:57 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 7fc51b00d39ad67002fcbd46c6f67431a8944ac0 to aaa5879ec174c2d6322106280c816943b9e4f015 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 20:41:31 to 01/20/2026 20:44:57 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 014e27881 - 2026-01-20 14:42:41 -0600 - 01/20/2026 14:42:41
Added in Other:
- DFFlagAlteredNaN = True | Mechanism: Changes how 'Not a Number' values are handled in calculations. | Purpose: Reduces errors in games that rely on numerical calculations, leading to a more stable experience.
- DFFlagSendBundledChunkSizeStat = True | Mechanism: Tracks and sends data about the size of bundled game assets. | Purpose: Helps developers understand asset loading times, improving game performance for players.
- FFlagAvatarPreviewerShortenAttributeName = True | Mechanism: Reduces the length of attribute names in the avatar preview tool. | Purpose: Makes it easier for players to read and understand avatar attributes.
- FFlagLuauCodegenVectorIdiv = True | Mechanism: Introduces a new way to handle vector division in the Luau programming language. | Purpose: Allows developers to create smoother and more efficient gameplay mechanics involving vectors.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 0015e24594d6ae231a9ae7234ba61217b1cfd23f to 7fc51b00d39ad67002fcbd46c6f67431a8944ac0 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 20:39:46 to 01/20/2026 20:41:31 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 0015e24594d6ae231a9ae7234ba61217b1cfd23f to 7fc51b00d39ad67002fcbd46c6f67431a8944ac0 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 20:39:46 to 01/20/2026 20:41:31 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagAlteredNaN_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T19:36:26) | Mechanism: Changes the handling of 'Not a Number' (NaN) values in calculations. | Purpose: Improves stability and predictability in scripts that deal with numerical data.
- DFFlagSendBundledChunkSizeStat_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T19:37:41) | Mechanism: Tracks the size of data chunks being sent in bundles. | Purpose: Helps developers optimize data transfer, leading to smoother gameplay and faster loading times.
- FFlagAvatarPreviewerShortenAttributeName_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T19:36:05) | Mechanism: Shortens the names of attributes in the avatar previewer. | Purpose: Makes it easier for players to read and understand avatar options.
- FFlagLuauCodegenVectorIdiv_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T19:39:43) | Mechanism: Improves how the Luau scripting language handles division for vector types. | Purpose: Enhances performance and accuracy for developers using vector math in their scripts.

## 2e058aee3 - 2026-01-20 14:40:23 -0600 - 01/20/2026 14:40:23
Added in Other:
- DFFlagReflectionServiceFixRootCrash_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T20:38:55 | Mechanism: Fixes a bug in the reflection service that caused crashes. | Purpose: Enhances game stability by preventing crashes related to the reflection service.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 4fd147ebbeb02903ad0d64eec7df54ac424ebcd9 to 0015e24594d6ae231a9ae7234ba61217b1cfd23f | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 20:36:38 to 01/20/2026 20:39:46 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 4fd147ebbeb02903ad0d64eec7df54ac424ebcd9 to 0015e24594d6ae231a9ae7234ba61217b1cfd23f | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 20:36:38 to 01/20/2026 20:39:46 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 07085bb16 - 2026-01-20 14:38:04 -0600 - 01/20/2026 14:38:04
Added in Other:
- FFlagCaptureUtilitiesCaptureParamsEnabled2 = True | Mechanism: Enables advanced parameters for capturing gameplay data. | Purpose: Allows for more detailed tracking and analysis of gameplay, improving game development and player experience.
- FFlagFixModelPreviewForUnifiedPurchaseModals = True | Mechanism: Corrects the model preview display in purchase dialogs. | Purpose: Ensures players see accurate previews when buying models.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 6009de4fefa8165ed4a3060e8d26e44555266da8 to 4fd147ebbeb02903ad0d64eec7df54ac424ebcd9 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 20:34:52 to 01/20/2026 20:36:38 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 6009de4fefa8165ed4a3060e8d26e44555266da8 to 4fd147ebbeb02903ad0d64eec7df54ac424ebcd9 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 20:34:52 to 01/20/2026 20:36:38 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagCaptureUtilitiesCaptureParamsEnabled2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T19:34:27) | Mechanism: Enables advanced parameters for capturing gameplay data. | Purpose: Provides developers with better tools to analyze gameplay, leading to improved player experiences.
- FFlagFixModelPreviewForUnifiedPurchaseModals_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T19:34:57) | Mechanism: Corrects issues with model previews in purchase windows. | Purpose: Ensures players can see accurate previews before buying items.

## cad442656 - 2026-01-20 14:35:46 -0600 - 01/20/2026 14:35:46
Added in Camera/UI:
- DFFlagSerializerReadBoolsAsUInts_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T20:33:47 | Mechanism: Changes how boolean values are read, treating them as unsigned integers. | Purpose: Improves data handling efficiency, leading to smoother gameplay experiences.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 808593e1261c71b2f287eb3e6906fdc5a589f81b to 6009de4fefa8165ed4a3060e8d26e44555266da8 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 20:26:26 to 01/20/2026 20:34:52 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 808593e1261c71b2f287eb3e6906fdc5a589f81b to 6009de4fefa8165ed4a3060e8d26e44555266da8 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 20:26:26 to 01/20/2026 20:34:52 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 595c63189 - 2026-01-20 14:29:00 -0600 - 01/20/2026 14:28:59
Added in Other:
- FFlagAXFixLookDetailsVR = True | Mechanism: Adjusts how look details are processed in virtual reality. | Purpose: Enhances the visual experience for players using VR headsets.
Added in Camera/UI:
- FFlagFixMissingIECUIForGrantedAssets = True | Mechanism: Fixes a bug that prevented certain user interface elements from showing for granted assets. | Purpose: Enhances user experience by ensuring all assets are properly displayed.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from c5fc2f9487aca1049eba9a3b30bde4bac7da0a6f to 808593e1261c71b2f287eb3e6906fdc5a589f81b | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 20:21:25 to 01/20/2026 20:26:26 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from c5fc2f9487aca1049eba9a3b30bde4bac7da0a6f to 808593e1261c71b2f287eb3e6906fdc5a589f81b | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 20:21:25 to 01/20/2026 20:26:26 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagAXFixLookDetailsVR_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T19:23:01) | Mechanism: Fixes issues with how details are displayed in virtual reality. | Purpose: Enhances the visual experience for players using VR headsets.
Removed in Camera/UI:
- FFlagFixMissingIECUIForGrantedAssets_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T19:23:18) | Mechanism: Fixes issues with user interface elements for granted assets. | Purpose: Ensures players can see and use all their granted assets properly.

## adb92c0be - 2026-01-20 14:22:08 -0600 - 01/20/2026 14:22:08
Added in Other:
- DFFlagSimDcdDeltaFixFlagLogic = True | Mechanism: Fixes the logic for delta changes in simulation data. | Purpose: Improves the accuracy and performance of game simulations for a smoother experience.
- FFlagCaptureStorageCanCaptureScreenshotCheck = True | Mechanism: Enables a check to see if a screenshot can be captured and stored. | Purpose: Improves the reliability of capturing and saving screenshots in games.
Changed in Other:
- DFIntMigrateTriangleMeshPartTimeLimit changed from 2 to 3 | Mechanism: Sets a time limit for migrating triangle mesh parts in the game engine. | Purpose: Ensures that the game runs efficiently by managing how long it takes to process complex shapes.
- DFStringFlagRepoGitHashDynamicString changed from 607fa38cd896fa6f14044552b7d3f9ae8e6945d9 to c5fc2f9487aca1049eba9a3b30bde4bac7da0a6f | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 20:11:53 to 01/20/2026 20:21:25 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 607fa38cd896fa6f14044552b7d3f9ae8e6945d9 to c5fc2f9487aca1049eba9a3b30bde4bac7da0a6f | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 20:11:53 to 01/20/2026 20:21:25 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagSimDcdDeltaFixFlagLogic_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T19:13:39) | Mechanism: Fixes logic related to delta calculations in simulations. | Purpose: Ensures smoother gameplay and more accurate game physics.
- DFIntMigrateTriangleMeshPartTimeLimit_Staged removed (was 3;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;false;347593854;2026-01-20T19:16:44) | Mechanism: Adjusts the time limit for processing triangle mesh parts in the game engine. | Purpose: Improves performance by optimizing how quickly complex shapes are handled.
- FFlagCaptureStorageCanCaptureScreenshotCheck_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T19:18:35) | Mechanism: Allows the system to check if a screenshot can be captured during storage operations. | Purpose: Ensures that players can take screenshots of their game experiences without issues.

## 455313679 - 2026-01-20 14:13:08 -0600 - 01/20/2026 14:13:08
Added in Other:
- DFFlagFixGetCaptureTmpDirectoryCrash = True | Mechanism: Fixes a crash related to accessing temporary directory for captures. | Purpose: Improves stability when capturing gameplay, preventing unexpected crashes.
- FFlagLuauCodegenNumIntFolds2 = True | Mechanism: Changes how integer folds are generated in Luau code. | Purpose: Improves performance and efficiency in scripts for developers.
- FFlagLuauCodegenSplitFloatExtra = True | Mechanism: Enhances the code generation process for floating-point numbers in Luau. | Purpose: Increases performance and efficiency for developers writing scripts.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 281a317b134a400000100eaff87b46af6754d2c7 to 607fa38cd896fa6f14044552b7d3f9ae8e6945d9 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 20:06:20 to 01/20/2026 20:11:53 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 281a317b134a400000100eaff87b46af6754d2c7 to 607fa38cd896fa6f14044552b7d3f9ae8e6945d9 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 20:06:20 to 01/20/2026 20:11:53 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagFixGetCaptureTmpDirectoryCrash_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T19:07:31) | Mechanism: Fixes a crash issue related to temporary directory access during capture. | Purpose: Ensures a more stable experience when capturing game footage.
- FFlagLuauCodegenNumIntFolds2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T19:06:52) | Mechanism: Optimizes the way integer folding is handled in Luau code generation. | Purpose: Improves performance and efficiency of scripts, leading to smoother gameplay.
- FFlagLuauCodegenSplitFloatExtra_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T19:06:26) | Mechanism: Improves the way floating-point numbers are handled in code generation. | Purpose: Enhances performance and accuracy for developers using Luau scripting.

## dfc704c07 - 2026-01-20 14:08:38 -0600 - 01/20/2026 14:08:37
Added in Other:
- FFlagAvatarPreviewerAvoidExtraRootPart = True | Mechanism: Removes an unnecessary root part from the avatar preview system. | Purpose: Improves the performance and accuracy of avatar previews for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from e580919c6f8c5685a71cf12d5324b98a7fe8fc4e to 281a317b134a400000100eaff87b46af6754d2c7 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 20:01:51 to 01/20/2026 20:06:20 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from e580919c6f8c5685a71cf12d5324b98a7fe8fc4e to 281a317b134a400000100eaff87b46af6754d2c7 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 20:01:51 to 01/20/2026 20:06:20 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagAvatarPreviewerAvoidExtraRootPart_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T19:03:46) | Mechanism: Removes an unnecessary root part from the avatar preview system. | Purpose: Provides a cleaner and more accurate avatar preview for players.

## 1763caffb - 2026-01-20 14:04:05 -0600 - 01/20/2026 14:04:05
Added in Other:
- DFFlagBezierUseCorrectIterationCount = True | Mechanism: Adjusts the algorithm for calculating curves to use the correct number of iterations. | Purpose: Improves the accuracy of curved paths in games, making them look smoother and more realistic.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from bcf01f6d9a5465c4e4c02612161ec063e959854e to e580919c6f8c5685a71cf12d5324b98a7fe8fc4e | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 20:00:49 to 01/20/2026 20:01:51 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from bcf01f6d9a5465c4e4c02612161ec063e959854e to e580919c6f8c5685a71cf12d5324b98a7fe8fc4e | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 20:00:49 to 01/20/2026 20:01:51 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagBezierUseCorrectIterationCount_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T18:55:17) | Mechanism: Adjusts the algorithm to use the correct number of iterations for Bezier curves. | Purpose: Improves the accuracy and smoothness of curves in game graphics, enhancing visual quality.

## 11e574689 - 2026-01-20 14:01:47 -0600 - 01/20/2026 14:01:47
Added in Other:
- DFIntTriangleMeshPartMigrationPerDMScale_Staged = 100000;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;false;1243995815;2026-01-20T19:59:53 | Mechanism: Migrates triangle mesh parts to a new system based on dynamic scaling. | Purpose: Improves the performance and appearance of 3D models in games.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 510e3e2a1a1807eb53e28cd5c65df07f05c2b993 to bcf01f6d9a5465c4e4c02612161ec063e959854e | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 19:51:31 to 01/20/2026 20:00:49 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 510e3e2a1a1807eb53e28cd5c65df07f05c2b993 to bcf01f6d9a5465c4e4c02612161ec063e959854e | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 19:51:31 to 01/20/2026 20:00:49 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 8d0578647 - 2026-01-20 13:52:48 -0600 - 01/20/2026 13:52:48
Added in Other:
- FFlagEnableCorescriptsProfiler = True | Mechanism: Enables profiling tools for core scripts to analyze performance. | Purpose: Helps developers optimize their games by identifying performance issues in core scripts.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 6404cf893b4cfc6637a4bc834d0ec4caa1e92b87 to 510e3e2a1a1807eb53e28cd5c65df07f05c2b993 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 19:46:30 to 01/20/2026 19:51:31 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 6404cf893b4cfc6637a4bc834d0ec4caa1e92b87 to 510e3e2a1a1807eb53e28cd5c65df07f05c2b993 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 19:46:30 to 01/20/2026 19:51:31 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagEnableCorescriptsProfiler_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T18:49:29) | Mechanism: Activates a tool for monitoring core scripts performance. | Purpose: Allows developers to identify and fix performance issues in core scripts, improving overall game performance.

## 9ed859568 - 2026-01-20 13:48:17 -0600 - 01/20/2026 13:48:17
Added in Other:
- DFFlagRbsAutocompleteAllowNonServiceChildrenOfDm = True | Mechanism: Allows autocomplete features to include non-service children in the Developer Marketplace. | Purpose: Makes it easier for developers to find and use assets when creating games.
- DFFlagRbsAutocompleteEnableGame = True | Mechanism: Enables autocomplete suggestions for game titles when searching. | Purpose: Helps players find games faster by suggesting titles as they type.
- FFlagAXInferCategorySelection = True | Mechanism: Automatically categorizes items based on user selections. | Purpose: Makes it easier for players to find relevant items quickly.
- FFlagPPVBackgroundParallelAssetLoading = True | Mechanism: Loads game assets in the background while the game is running. | Purpose: Reduces waiting time and improves gameplay experience.
Added in Physics:
- DFFlagSimOptimizeHumanoidRunning2 = True | Mechanism: Optimizes the simulation of humanoid running animations and physics. | Purpose: Makes character movements smoother and more realistic, enhancing gameplay immersion for players.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 4ee5d0075e893b486c6be7cebca492fd1951b241 to 6404cf893b4cfc6637a4bc834d0ec4caa1e92b87 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 19:41:53 to 01/20/2026 19:46:30 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 4ee5d0075e893b486c6be7cebca492fd1951b241 to 6404cf893b4cfc6637a4bc834d0ec4caa1e92b87 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 19:41:53 to 01/20/2026 19:46:30 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagRbsAutocompleteAllowNonServiceChildrenOfDm_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;false;234075857;2026-01-20T18:40:46) | Mechanism: Allows autocomplete to include non-service children in the data model. | Purpose: Helps developers find and use more elements easily when scripting.
- DFFlagRbsAutocompleteEnableGame_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;false;234075857;2026-01-20T18:40:46) | Mechanism: Enables autocomplete suggestions for game searches. | Purpose: Helps players find games faster by suggesting titles as they type.
- FFlagAXInferCategorySelection_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T18:40:30) | Mechanism: Automatically infers category selections based on user input. | Purpose: Makes it easier for players to find and select categories when creating or browsing content.
- FFlagPPVBackgroundParallelAssetLoading_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T18:40:19) | Mechanism: Tests background asset loading for better performance. | Purpose: Aims to enhance the speed and efficiency of loading game content.
Removed in Physics:
- DFFlagSimOptimizeHumanoidRunning2_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T18:42:40) | Mechanism: Optimizes the simulation of humanoid character running mechanics. | Purpose: Provides smoother and more responsive character movement for players.

## e4d5d74d9 - 2026-01-20 13:43:45 -0600 - 01/20/2026 13:43:44
Added in Other:
- DFFlagVideoSourceStatusCounters = True | Mechanism: Tracks the status of video sources for analytics. | Purpose: Provides insights into video performance, helping improve user experience.
- FFlagSeparateInactivePlaceholderGroups = True | Mechanism: Separates inactive placeholder groups in the development environment. | Purpose: Makes it easier for developers to manage and organize their assets.
- FFlagStreamingPauseFlickerStats = True | Mechanism: Adjusts how streaming pause statistics are displayed. | Purpose: Reduces visual flickering during streaming pauses, enhancing user experience.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 088124484f311e992948ea8f2f28619f7b9da0e3 to 4ee5d0075e893b486c6be7cebca492fd1951b241 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 19:40:29 to 01/20/2026 19:41:53 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 088124484f311e992948ea8f2f28619f7b9da0e3 to 4ee5d0075e893b486c6be7cebca492fd1951b241 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 19:40:29 to 01/20/2026 19:41:53 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- DFFlagVideoSourceStatusCounters_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T18:36:22) | Mechanism: Tracks the status of video sources for better analytics. | Purpose: Provides insights into video performance and issues for smoother playback.
- FFlagSeparateInactivePlaceholderGroups_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T18:37:47) | Mechanism: Separates inactive placeholder groups in the game engine. | Purpose: Improves organization and performance of game assets.
- FFlagStreamingPauseFlickerStats_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T18:39:11) | Mechanism: Enables tracking of flicker events during streaming pauses. | Purpose: Helps improve the stability and performance of games during streaming.

## 75425a927 - 2026-01-20 13:41:25 -0600 - 01/20/2026 13:41:25
Added in Other:
- DFFlagSendBundledChunkSizeStat_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T19:37:41 | Mechanism: Tracks the size of data chunks being sent in bundles. | Purpose: Helps developers optimize data transfer, leading to smoother gameplay and faster loading times.
- FFlagLuauCodegenVectorIdiv_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T19:39:43 | Mechanism: Improves how the Luau scripting language handles division for vector types. | Purpose: Enhances performance and accuracy for developers using vector math in their scripts.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 9696d735f3f5baf99afc358af42cf1fd53bd9a7e to 088124484f311e992948ea8f2f28619f7b9da0e3 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 19:37:43 to 01/20/2026 19:40:29 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 9696d735f3f5baf99afc358af42cf1fd53bd9a7e to 088124484f311e992948ea8f2f28619f7b9da0e3 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 19:37:43 to 01/20/2026 19:40:29 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## ea612ea09 - 2026-01-20 13:39:07 -0600 - 01/20/2026 13:39:06
Added in Other:
- DFFlagAlteredNaN_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T19:36:26 | Mechanism: Changes the handling of 'Not a Number' (NaN) values in calculations. | Purpose: Improves stability and predictability in scripts that deal with numerical data.
- FFlagAvatarPreviewerShortenAttributeName_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T19:36:05 | Mechanism: Shortens the names of attributes in the avatar previewer. | Purpose: Makes it easier for players to read and understand avatar options.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from a3197d2a82e83edf7291f390689a7a4ef9464fa2 to 9696d735f3f5baf99afc358af42cf1fd53bd9a7e | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 19:36:11 to 01/20/2026 19:37:43 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from a3197d2a82e83edf7291f390689a7a4ef9464fa2 to 9696d735f3f5baf99afc358af42cf1fd53bd9a7e | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 19:36:11 to 01/20/2026 19:37:43 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## 975697bb7 - 2026-01-20 13:36:48 -0600 - 01/20/2026 13:36:47
Added in Other:
- FFlagCaptureUtilitiesCaptureParamsEnabled2_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T19:34:27 | Mechanism: Enables advanced parameters for capturing gameplay data. | Purpose: Provides developers with better tools to analyze gameplay, leading to improved player experiences.
- FFlagFixModelPreviewForUnifiedPurchaseModals_Staged = true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T19:34:57 | Mechanism: Corrects issues with model previews in purchase windows. | Purpose: Ensures players can see accurate previews before buying items.
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from a175f09be882274081cfcf4abceab5de76224036 to a3197d2a82e83edf7291f390689a7a4ef9464fa2 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 19:31:58 to 01/20/2026 19:36:11 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from a175f09be882274081cfcf4abceab5de76224036 to a3197d2a82e83edf7291f390689a7a4ef9464fa2 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 19:31:58 to 01/20/2026 19:36:11 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.

## ab42a7b76 - 2026-01-20 13:34:28 -0600 - 01/20/2026 13:34:28
Changed in Other:
- DFStringFlagRepoGitHashDynamicString changed from 47d66f28ec5842b5297bf34245ca4867a594426c to a175f09be882274081cfcf4abceab5de76224036 | Mechanism: Stores a dynamic string related to the version control of the code. | Purpose: Helps developers track changes and updates in the game more efficiently.
- DFStringFlipTimeStampDynamicString changed from 01/20/2026 19:27:14 to 01/20/2026 19:31:58 | Mechanism: Updates dynamic strings with timestamp information. | Purpose: Allows players to see real-time updates or changes in game events, enhancing gameplay immersion.
- FStringFlagRepoGitHashFastString changed from 47d66f28ec5842b5297bf34245ca4867a594426c to a175f09be882274081cfcf4abceab5de76224036 | Mechanism: Uses a fast string representation of the Git hash for version control. | Purpose: Improves the efficiency of version tracking, ensuring smoother updates for players.
- FStringFlipTimeStampFastString changed from 01/20/2026 19:27:14 to 01/20/2026 19:31:58 | Mechanism: Optimizes the way timestamps are handled in strings for faster processing. | Purpose: Improves the speed of time-related operations in games, making them run smoother.
Removed in Other:
- FFlagAXRootRFYMigration_Staged removed (was false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T19:17:08) | Mechanism: Migrates the accessibility root to a new system for better compatibility. | Purpose: Improves accessibility features for players, making the game easier to navigate for everyone.

## b351eae37 - 2026-01-20 13:32:10 -0600 - 01/20/2026 13:32:10
Added in Other:
- DFFlagImprovedFindFirstAncestorIf = True | Mechanism: Optimizes the method for finding the first ancestor object in the hierarchy. | Purpose: Increases performance and reliability when scripts need to locate parent objects.
Changed in Other:
- FFlagAXEnableSlotsFtux2 changed from True to False | Mechanism: Activates a new feature for slot management in the user interface. | Purpose: Enhances the user experience by providing better organization and access to game slots.
Removed in Other:
- DFFlagImprovedFindFirstAncestorIf_Staged removed (was true;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T18:29:06) | Mechanism: Enhances the method for finding the first ancestor in the object hierarchy. | Purpose: Improves script performance and reliability, leading to smoother gameplay.
- FFlagAXEnableSlotsFtux2_Staged removed (was false;SteadyState;10;15;Rollout;100;30;SteadyState;100;15;Promote;2026-01-20T18:28:32) | Mechanism: Enables a new feature for slot-based tutorials in the game. | Purpose: Improves the onboarding experience for new players by guiding them through game mechanics.