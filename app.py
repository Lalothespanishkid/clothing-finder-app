
import streamlit as st
import json
from datetime import datetime, timedelta
import sqlite3
import csv
from io import StringIO

# Page configuration
st.set_page_config(
    page_title="Social Media Performance Tracker",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'data' not in st.session_state:
    st.session_state.data = []

# Database functions
def init_db():
    conn = sqlite3.connect('social_media_tracker.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS daily_entries
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  date TEXT, platforms TEXT, followers_gained INTEGER,
                  likes INTEGER, comments INTEGER, impressions INTEGER,
                  post_type TEXT, problems TEXT, thoughts TEXT, next_actions TEXT)''')
    conn.commit()
    conn.close()

def save_entry(entry_data):
    conn = sqlite3.connect('social_media_tracker.db')
    c = conn.cursor()
    c.execute('''INSERT INTO daily_entries 
                 (date, platforms, followers_gained, likes, comments, impressions, 
                  post_type, problems, thoughts, next_actions)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', entry_data)
    conn.commit()
    conn.close()

def load_entries():
    conn = sqlite3.connect('social_media_tracker.db')
    c = conn.cursor()
    c.execute("SELECT * FROM daily_entries ORDER BY date DESC")
    rows = c.fetchall()
    conn.close()
    
    data = []
    for row in rows:
        data.append({
            'id': row[0],
            'date': datetime.strptime(row[1], '%Y-%m-%d').date(),
            'platforms': json.loads(row[2]) if row[2] else [],
            'followers_gained': row[3],
            'likes': row[4],
            'comments': row[5],
            'impressions': row[6],
            'post_type': json.loads(row[7]) if row[7] else [],
            'problems': row[8],
            'thoughts': row[9],
            'next_actions': row[10]
        })
    return data

# Initialize database
init_db()

# Load existing data
if not st.session_state.data:
    st.session_state.data = load_entries()

# Available platforms and post types
PLATFORMS = ["Instagram", "TikTok", "Threads", "X (Twitter)", "Facebook", "YouTube", "LinkedIn", "OnlyFans", "Fanvue"]
POST_TYPES = ["Video", "Carousel", "Story", "Reel", "Post", "Live", "Story", "Poll", "Tease", "Lifestyle", "Selfies", "Memes"]

# Helper functions for data analysis
def calculate_totals(data):
    total_followers = sum(entry['followers_gained'] for entry in data)
    total_likes = sum(entry['likes'] for entry in data)
    total_comments = sum(entry['comments'] for entry in data)
    total_impressions = sum(entry['impressions'] for entry in data)
    return total_followers, total_likes, total_comments, total_impressions

def get_platform_counts(data):
    platform_counts = {}
    for entry in data:
        for platform in entry['platforms']:
            platform_counts[platform] = platform_counts.get(platform, 0) + 1
    return platform_counts

def filter_data_by_date(data, start_date, end_date):
    return [entry for entry in data if start_date <= entry['date'] <= end_date]

def filter_data_by_platform(data, selected_platforms):
    if not selected_platforms:
        return data
    return [entry for entry in data if any(platform in entry['platforms'] for platform in selected_platforms)]

def filter_data_by_metrics(data, min_followers, min_likes, min_impressions):
    return [entry for entry in data if 
            entry['followers_gained'] >= min_followers and 
            entry['likes'] >= min_likes and 
            entry['impressions'] >= min_impressions]

# Sidebar for navigation
st.sidebar.title("📊 Social Media Tracker")
page = st.sidebar.selectbox(
    "Choose a page:",
    ["📝 Daily Entry", "📊 Dashboard", "📈 Analytics", "🔍 Data Explorer"]
)

# Daily Entry Page
if page == "📝 Daily Entry":
    st.title("📝 Daily Social Media Entry")
    st.write("Log your daily social media activity and metrics")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Date selection
        entry_date = st.date_input("📅 Date", value=datetime.now())
        
        # Platforms used
        platforms_used = st.multiselect(
            "📱 Platforms Used",
            options=PLATFORMS,
            help="Select all platforms where you posted content today"
        )
        
        # Post type breakdown
        post_types = st.multiselect(
            "📝 Post Types",
            options=POST_TYPES,
            help="What types of content did you post?"
        )
        
        # Metrics
        st.subheader("📊 Engagement Metrics")
        col_metrics1, col_metrics2 = st.columns(2)
        
        with col_metrics1:
            followers_gained = st.number_input("👥 New Followers", min_value=0, value=0)
            likes = st.number_input("❤️ Total Likes", min_value=0, value=0)
            comments = st.number_input("💬 Total Comments", min_value=0, value=0)
        
        with col_metrics2:
            impressions = st.number_input("👁️ Total Impressions/Views", min_value=0, value=0)
        
        # Additional fields
        problems = st.text_area("🔧 Problems/Issues", placeholder="Any technical issues or challenges today?")
        thoughts = st.text_area("💭 Thoughts/Reflections", placeholder="What worked well? What could be improved?")
        next_actions = st.text_area("🎯 Next Actions", placeholder="What's your plan for tomorrow?")
    
    with col2:
        st.subheader("📋 Quick Summary")
        if platforms_used:
            st.write(f"**Platforms:** {', '.join(platforms_used)}")
        if post_types:
            st.write(f"**Content Types:** {', '.join(post_types)}")
        if followers_gained > 0:
            st.success(f"🎉 +{followers_gained} new followers!")
        if likes > 0:
            st.info(f"❤️ {likes} total likes")
        if impressions > 0:
            st.info(f"👁️ {impressions} impressions")
    
    # Submit button
    if st.button("💾 Save Entry", type="primary"):
        if not platforms_used:
            st.error("Please select at least one platform")
        else:
            # Prepare data
            entry_data = (
                entry_date.strftime('%Y-%m-%d'),
                json.dumps(platforms_used),
                followers_gained,
                likes,
                comments,
                impressions,
                json.dumps(post_types),
                problems,
                thoughts,
                next_actions
            )
            
            # Save to database
            save_entry(entry_data)
            
            # Update session state
            new_entry = {
                'id': len(st.session_state.data) + 1,
                'date': entry_date,
                'platforms': platforms_used,
                'followers_gained': followers_gained,
                'likes': likes,
                'comments': comments,
                'impressions': impressions,
                'post_type': post_types,
                'problems': problems,
                'thoughts': thoughts,
                'next_actions': next_actions
            }
            st.session_state.data.insert(0, new_entry)
            
            st.success("✅ Entry saved successfully!")
            st.balloons()

# Dashboard Page
elif page == "📊 Dashboard":
    st.title("📊 Social Media Dashboard")
    
    if not st.session_state.data:
        st.info("No data yet. Add some daily entries to see your dashboard!")
    else:
        # Key metrics summary
        st.subheader("📈 Key Metrics Overview")
        
        total_followers, total_likes, total_comments, total_impressions = calculate_totals(st.session_state.data)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Followers Gained", f"+{total_followers:,}")
        with col2:
            st.metric("Total Likes", f"{total_likes:,}")
        with col3:
            st.metric("Total Comments", f"{total_comments:,}")
        with col4:
            st.metric("Total Impressions", f"{total_impressions:,}")
        
        # Recent entries table
        st.subheader("📋 Recent Entries")
        
        # Create a simple table display
        if st.session_state.data:
            table_data = []
            for entry in st.session_state.data[:10]:  # Show last 10 entries
                table_data.append({
                    'Date': entry['date'].strftime('%Y-%m-%d'),
                    'Platforms': ', '.join(entry['platforms']),
                    'Followers': entry['followers_gained'],
                    'Likes': entry['likes'],
                    'Comments': entry['comments'],
                    'Impressions': entry['impressions'],
                    'Post Types': ', '.join(entry['post_type'])
                })
            
            # Display as a simple table
            for i, row in enumerate(table_data):
                if i == 0:  # Header
                    st.write("| Date | Platforms | Followers | Likes | Comments | Impressions | Post Types |")
                    st.write("|------|-----------|-----------|-------|----------|-------------|------------|")
                
                st.write(f"| {row['Date']} | {row['Platforms']} | {row['Followers']} | {row['Likes']} | {row['Comments']} | {row['Impressions']} | {row['Post Types']} |")
        
        # Platform breakdown
        st.subheader("📱 Platform Activity")
        platform_counts = get_platform_counts(st.session_state.data)
        
        if platform_counts:
            # Create a simple bar chart using text
            max_count = max(platform_counts.values()) if platform_counts else 1
            
            for platform, count in sorted(platform_counts.items(), key=lambda x: x[1], reverse=True):
                bar_length = int((count / max_count) * 50)  # Scale to 50 characters
                bar = "█" * bar_length
                st.write(f"**{platform}:** {bar} {count} posts")
        
        # Engagement rate
        if total_impressions > 0:
            engagement_rate = (total_likes + total_comments) / total_impressions * 100
            st.subheader("🎯 Engagement Rate")
            st.metric("Overall Engagement Rate", f"{engagement_rate:.2f}%")

# Analytics Page
elif page == "📈 Analytics":
    st.title("📈 Analytics & Trends")
    
    if not st.session_state.data:
        st.info("No data yet. Add some daily entries to see analytics!")
    else:
        # Date range filter
        st.subheader("📅 Date Range Filter")
        col1, col2 = st.columns(2)
        
        min_date = min(entry['date'] for entry in st.session_state.data)
        max_date = max(entry['date'] for entry in st.session_state.data)
        
        with col1:
            start_date = st.date_input("Start Date", value=min_date)
        with col2:
            end_date = st.date_input("End Date", value=max_date)
        
        # Filter data by date range
        filtered_data = filter_data_by_date(st.session_state.data, start_date, end_date)
        
        if filtered_data:
            # Growth trends summary
            st.subheader("📈 Growth Trends Summary")
            
            # Calculate trends
            total_followers, total_likes, total_comments, total_impressions = calculate_totals(filtered_data)
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Total Followers in Period", f"+{total_followers:,}")
                st.metric("Total Likes in Period", f"{total_likes:,}")
            with col2:
                st.metric("Total Comments in Period", f"{total_comments:,}")
                st.metric("Total Impressions in Period", f"{total_impressions:,}")
            
            # Best performing days
            st.subheader("🏆 Best Performing Days")
            
            if filtered_data:
                best_followers = max(filtered_data, key=lambda x: x['followers_gained'])
                best_likes = max(filtered_data, key=lambda x: x['likes'])
                best_impressions = max(filtered_data, key=lambda x: x['impressions'])
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.info(f"**Best Day for Followers:** {best_followers['date'].strftime('%Y-%m-%d')} (+{best_followers['followers_gained']})")
                with col2:
                    st.info(f"**Best Day for Likes:** {best_likes['date'].strftime('%Y-%m-%d')} ({best_likes['likes']} likes)")
                with col3:
                    st.info(f"**Best Day for Impressions:** {best_impressions['date'].strftime('%Y-%m-%d')} ({best_impressions['impressions']} impressions)")
            
            # Platform performance
            st.subheader("📱 Platform Performance")
            platform_counts = get_platform_counts(filtered_data)
            
            if platform_counts:
                for platform, count in sorted(platform_counts.items(), key=lambda x: x[1], reverse=True):
                    # Calculate platform-specific metrics
                    platform_entries = [entry for entry in filtered_data if platform in entry['platforms']]
                    platform_followers = sum(entry['followers_gained'] for entry in platform_entries)
                    platform_likes = sum(entry['likes'] for entry in platform_entries)
                    
                    st.write(f"**{platform}:** {count} posts, +{platform_followers} followers, {platform_likes} likes")

# Data Explorer Page
elif page == "🔍 Data Explorer":
    st.title("🔍 Data Explorer & Filtering")
    
    if not st.session_state.data:
        st.info("No data yet. Add some daily entries to explore!")
    else:
        # Advanced filtering
        st.subheader("🔍 Advanced Filters")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Platform filter
            selected_platforms = st.multiselect(
                "Filter by Platform",
                options=PLATFORMS,
                help="Show only entries from selected platforms"
            )
            
            # Date range filter
            min_date = min(entry['date'] for entry in st.session_state.data)
            max_date = max(entry['date'] for entry in st.session_state.data)
            date_range = st.date_input(
                "Date Range",
                value=(min_date, max_date),
                help="Select date range to filter data"
            )
        
        with col2:
            # Metric filters
            min_followers = st.number_input("Min Followers Gained", min_value=0, value=0)
            min_likes = st.number_input("Min Likes", min_value=0, value=0)
            min_impressions = st.number_input("Min Impressions", min_value=0, value=0)
        
        # Apply filters
        filtered_data = st.session_state.data.copy()
        
        if selected_platforms:
            filtered_data = filter_data_by_platform(filtered_data, selected_platforms)
        
        if len(date_range) == 2:
            filtered_data = filter_data_by_date(filtered_data, date_range[0], date_range[1])
        
        filtered_data = filter_data_by_metrics(filtered_data, min_followers, min_likes, min_impressions)
        
        # Display filtered results
        st.subheader(f"📊 Filtered Results ({len(filtered_data)} entries)")
        
        if filtered_data:
            # Summary statistics
            total_followers, total_likes, total_impressions = calculate_totals(filtered_data)[:3]
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Followers", f"+{total_followers:,}")
            with col2:
                st.metric("Total Likes", f"{total_likes:,}")
            with col3:
                st.metric("Total Impressions", f"{total_impressions:,}")
            
            # Filtered data table
            st.subheader("📋 Filtered Data")
            for entry in filtered_data:
                with st.expander(f"{entry['date'].strftime('%Y-%m-%d')} - {', '.join(entry['platforms'])}"):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**Platforms:** {', '.join(entry['platforms'])}")
                        st.write(f"**Post Types:** {', '.join(entry['post_type'])}")
                        st.write(f"**Followers Gained:** {entry['followers_gained']}")
                    with col2:
                        st.write(f"**Likes:** {entry['likes']}")
                        st.write(f"**Comments:** {entry['comments']}")
                        st.write(f"**Impressions:** {entry['impressions']}")
                    
                    if entry['problems']:
                        st.write(f"**Problems:** {entry['problems']}")
                    if entry['thoughts']:
                        st.write(f"**Thoughts:** {entry['thoughts']}")
                    if entry['next_actions']:
                        st.write(f"**Next Actions:** {entry['next_actions']}")
            
            # Export options
            st.subheader("📤 Export Data")
            
            # Create CSV data
            csv_data = StringIO()
            if filtered_data:
                fieldnames = ['Date', 'Platforms', 'Followers_Gained', 'Likes', 'Comments', 'Impressions', 'Post_Type', 'Problems', 'Thoughts', 'Next_Actions']
                writer = csv.DictWriter(csv_data, fieldnames=fieldnames)
                writer.writeheader()
                
                for entry in filtered_data:
                    writer.writerow({
                        'Date': entry['date'].strftime('%Y-%m-%d'),
                        'Platforms': ', '.join(entry['platforms']),
                        'Followers_Gained': entry['followers_gained'],
                        'Likes': entry['likes'],
                        'Comments': entry['comments'],
                        'Impressions': entry['impressions'],
                        'Post_Type': ', '.join(entry['post_type']),
                        'Problems': entry['problems'] or '',
                        'Thoughts': entry['thoughts'] or '',
                        'Next_Actions': entry['next_actions'] or ''
                    })
            
            st.download_button(
                label="📥 Download CSV",
                data=csv_data.getvalue(),
                file_name=f"social_media_data_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
        else:
            st.warning("No data matches your current filters. Try adjusting the criteria.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Social Media Performance Tracker v1.0")
