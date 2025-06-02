usersQuery = """
        query Users($next: String) {
						users(
							first: 100
							after: $next
						) {
							pageInfo {
								hasNextPage
								endCursor
							}
							nodes {
								id
								name
								active
								admin
                                archivedAt
                                avatarUrl
                                calendarHash
								createdAt
                                createdIssueCount
								description
                                disableReason
								displayName
                                inviteHash
                                isMe
								email
								guest
								lastSeen
								organization {
									id
									name
								}
								statusLabel
								timezone
								updatedAt
								url
                                statusEmoji
                                statusUntilAt
							}
						}
					}
        """
