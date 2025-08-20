# 📊 Social Media Performance Tracker

A comprehensive, standalone web application that helps you track, analyze, and visualize your daily social media performance across multiple platforms. **No installation required - runs in any modern web browser!**

## 🎯 Features

### Core Functionality
- **Daily Entry Logging**: Log your daily social media activity with detailed metrics
- **Multi-Platform Support**: Track activity across Instagram, TikTok, Threads, X (Twitter), Facebook, YouTube, LinkedIn, OnlyFans, and Fanvue
- **Content Type Breakdown**: Categorize posts by type (Video, Carousel, Story, Reel, Live, etc.)
- **Engagement Metrics**: Track followers gained, likes, comments, and impressions
- **Reflection Fields**: Log problems, thoughts, and next actions for continuous improvement

### Analytics & Visualization
- **Real-time Dashboard**: View key metrics and recent entries at a glance
- **Trend Analysis**: Summary statistics and performance insights over time
- **Platform Performance**: Compare activity and engagement across different platforms
- **Engagement Rate Calculation**: Automatic calculation of overall engagement rates
- **Best Performance Tracking**: Identify your top-performing days and content

### Data Management
- **Advanced Filtering**: Filter by platform, date range, and metric thresholds
- **Data Export**: Download filtered data as CSV for external analysis
- **Local Storage**: Data is saved in your browser's localStorage (no server required)
- **Search & Explore**: Powerful data exploration tools to find insights

## 🚀 Getting Started

### Prerequisites
- Any modern web browser (Chrome, Firefox, Safari, Edge)
- **No installation required!**

### Installation & Usage

1. **Download the files** to your computer
2. **Open `index.html`** in your web browser
3. **Start tracking!** The app will work immediately

That's it! The application runs entirely in your browser with no external dependencies.

## 📱 How to Use

### 1. Daily Entry Page
- **Date Selection**: Choose the date for your entry (defaults to today)
- **Platforms**: Click to select all platforms where you posted content
- **Content Types**: Click to select the types of content you posted
- **Metrics**: Enter your engagement numbers (followers, likes, comments, impressions)
- **Reflection**: Add notes about problems, thoughts, and next actions
- **Save**: Click "Save Entry" to store your data

### 2. Dashboard Page
- **Overview Metrics**: See totals for followers gained, likes, comments, and impressions
- **Recent Entries**: View your latest 10 entries in a table format
- **Platform Activity**: Visual bar charts showing posts per platform
- **Engagement Rate**: Overall engagement rate calculation

### 3. Analytics Page
- **Date Range Display**: Shows the full range of your data
- **Growth Trends Summary**: Period totals for all metrics
- **Best Performing Days**: Discover your top days for followers and likes
- **Platform Performance**: Detailed breakdown by platform

### 4. Data Explorer Page
- **Advanced Filtering**: Filter by platform and metric thresholds
- **Filtered Results**: View and analyze specific data subsets
- **Data Export**: Download filtered data as CSV files

## 🗄️ Data Structure

The application stores the following information for each daily entry:

| Field | Type | Description |
|-------|------|-------------|
| Date | Date | The date of the entry |
| Platforms | Multi-select | Social media platforms used |
| Followers_Gained | Number | New followers acquired |
| Likes | Number | Total likes received |
| Comments | Number | Total comments received |
| Impressions | Number | Total reach/views |
| Post_Type | Multi-select | Types of content posted |
| Problems | Text | Issues or challenges encountered |
| Thoughts | Text | Reflections and insights |
| Next | Text | Future actions and plans |

## 🔧 Customization

### Adding New Platforms
Edit the platforms array in the HTML file:
```html
<div class="multiselect-option" onclick="toggleOption(this, 'Your New Platform')">Your New Platform</div>
```

### Adding New Post Types
Edit the post types array in the HTML file:
```html
<div class="multiselect-option" onclick="toggleOption(this, 'Your New Type')">Your New Type</div>
```

### Modifying Metrics
Add new metric fields by updating the form and JavaScript code in the HTML file.

## 📊 Data Export & Backup

- **CSV Export**: Use the Data Explorer page to export filtered data
- **Local Storage**: Data is automatically saved in your browser
- **Data Migration**: Export to CSV and import into other tools like Excel, Google Sheets, or analytics platforms
- **Backup**: Your data persists in the browser until you clear browser data

## 🎨 UI Features

- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Modern Interface**: Clean, intuitive design with smooth animations
- **Interactive Elements**: Hover effects, smooth transitions, and visual feedback
- **Real-time Updates**: See changes immediately after saving entries
- **Tab Navigation**: Easy switching between different views

## 🔍 Tips for Best Results

1. **Be Consistent**: Log your entries daily for the most accurate insights
2. **Use All Fields**: Fill in reflection fields to track what works and what doesn't
3. **Regular Analysis**: Check the Analytics page weekly to spot trends
4. **Platform Comparison**: Use the Dashboard to see which platforms drive the best engagement
5. **Export Data**: Regularly export your data for external analysis and backup
6. **Browser Compatibility**: Use the same browser consistently to maintain data

## 🚧 Troubleshooting

### Common Issues

**Data not saving:**
- Ensure JavaScript is enabled in your browser
- Check that you're using the same browser consistently
- Clear browser cache and try again

**App not working:**
- Make sure you're opening the `index.html` file directly in a browser
- Try a different browser if issues persist
- Ensure your browser supports modern JavaScript features

**Data lost:**
- Check if you cleared browser data or localStorage
- Export your data regularly as a backup
- Use the same browser and device consistently

**Performance issues:**
- Close other browser tabs
- Clear browser cache
- Restart your browser

## 🔮 Future Enhancements

Potential features for future versions:
- **Goal Setting**: Set and track follower/engagement goals
- **Content Calendar**: Plan and schedule future posts
- **Competitor Analysis**: Compare your performance with industry benchmarks
- **Automated Insights**: AI-powered recommendations based on your data
- **Integration**: Connect with social media APIs for automatic data import
- **Cloud Sync**: Save data to cloud storage for cross-device access
- **Advanced Charts**: More sophisticated visualizations and trend analysis

## 🌐 Browser Compatibility

- **Chrome**: 60+ ✅
- **Firefox**: 55+ ✅
- **Safari**: 12+ ✅
- **Edge**: 79+ ✅
- **Mobile Browsers**: iOS Safari, Chrome Mobile ✅

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve the application.

---

**Built with ❤️ using HTML, CSS, and JavaScript | Social Media Performance Tracker v1.0**

**No installation required - just open in your browser and start tracking!**