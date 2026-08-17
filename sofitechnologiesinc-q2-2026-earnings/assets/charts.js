(function () {
  'use strict';
  var rootStyle = getComputedStyle(document.documentElement);
  function cssVar(name, fallback) {
    var v = rootStyle.getPropertyValue(name);
    v = v ? v.trim() : '';
    return v || fallback;
  }
  var palette = {
    primary: cssVar('--accent', '#0071e3'),
    accent: cssVar('--accent2', '#34c759'),
    positive: cssVar('--accent2', '#34c759'),
    negative: cssVar('--neg', '#d93025'),
    warn: cssVar('--warn', '#ea8600'),
    neutral: cssVar('--muted', '#6e6e73'),
    text: cssVar('--ink', '#1d1d1f'),
    grid: cssVar('--rule', '#d2d2d7'),
    series1: '#0071e3',
    series2: '#34c759',
    series3: '#ff9500',
    series4: '#af52de',
    series5: '#ff3b30'
  };
  var isMobile = window.innerWidth <= 700;
  function fs(base) { return isMobile ? Math.round(base * 0.86) : base; }

  // ============================================================
  // 1. chart-revenue-trend: 营收与净利润趋势（柱状+折线，双Y轴）
  // ============================================================
  var chart1El = document.getElementById('chart-revenue-trend');
  if (chart1El) {
    var chart1 = echarts.init(chart1El, null, { renderer: 'svg' });
    chart1.setOption({
      animation: false,
      color: [palette.series1, palette.series2],
      tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
      legend: { data: ['营收（亿美元）', '净利润（亿美元）'], top: 5, textStyle: { fontSize: fs(12) } },
      grid: { left: isMobile ? '8%' : '6%', right: isMobile ? '12%' : '8%', top: 50, bottom: 40 },
      xAxis: {
        type: 'category',
        data: ['Q4 2024', 'Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025', 'Q1 2026', 'Q2 2026'],
        axisLabel: { fontSize: fs(11), rotate: isMobile ? 30 : 0 },
        axisLine: { lineStyle: { color: palette.grid } }
      },
      yAxis: [
        { type: 'value', name: '营收(亿$)', position: 'left', nameTextStyle: { fontSize: fs(11) }, axisLabel: { fontSize: fs(11) }, splitLine: { lineStyle: { color: palette.grid } } },
        { type: 'value', name: '净利润(亿$)', position: 'right', nameTextStyle: { fontSize: fs(11) }, axisLabel: { fontSize: fs(11) }, splitLine: { show: false } }
      ],
      series: [
        { name: '营收（亿美元）', type: 'bar', yAxisIndex: 0, data: [10.08, 10.37, 11.30, 12.68, 13.35, 14.08, 12.20], itemStyle: { color: palette.series1 }, barWidth: '40%' },
        { name: '净利润（亿美元）', type: 'line', yAxisIndex: 1, data: [3.32, 0.71, 0.97, 1.39, 1.74, 1.67, 1.57], itemStyle: { color: palette.series2 }, lineStyle: { width: 2.5 }, symbol: 'circle', symbolSize: 7, smooth: true }
      ]
    });
    window.addEventListener('resize', function() { chart1.resize(); });
  }

  // ============================================================
  // 2. chart-revenue-mix: 营收构成（饼图/环形）
  // ============================================================
  var chart2El = document.getElementById('chart-revenue-mix');
  if (chart2El) {
    var chart2 = echarts.init(chart2El, null, { renderer: 'svg' });
    chart2.setOption({
      animation: false,
      color: [palette.series1, palette.series2, palette.series3, palette.series4],
      tooltip: { trigger: 'item', formatter: '{b}: {c}亿$ ({d}%)' },
      legend: { orient: isMobile ? 'horizontal' : 'vertical', right: isMobile ? 'center' : 10, top: isMobile ? 'bottom' : 'middle', textStyle: { fontSize: fs(12) } },
      series: [{
        name: '营收构成',
        type: 'pie',
        radius: ['40%', '70%'],
        center: isMobile ? ['50%', '42%'] : ['40%', '50%'],
        avoidLabelOverlap: false,
        label: { show: true, formatter: '{b}\n{d}%', fontSize: fs(11) },
        labelLine: { show: true },
        data: [
          { value: 7.88, name: '净利息收入' },
          { value: 1.65, name: '贷款平台收入' },
          { value: 1.62, name: '金融服务收入' },
          { value: 1.05, name: '技术平台收入' }
        ]
      }]
    });
    window.addEventListener('resize', function() { chart2.resize(); });
  }

  // ============================================================
  // 3. chart-margin-trend: 利润率趋势（多折线）
  // ============================================================
  var chart3El = document.getElementById('chart-margin-trend');
  if (chart3El) {
    var chart3 = echarts.init(chart3El, null, { renderer: 'svg' });
    chart3.setOption({
      animation: false,
      color: [palette.series1, palette.series3, palette.series2, palette.series4],
      tooltip: { trigger: 'axis' },
      legend: { data: ['毛利率', '营业利润率', '净利率', 'ROE'], top: 5, textStyle: { fontSize: fs(12) } },
      grid: { left: isMobile ? '10%' : '8%', right: '5%', top: 50, bottom: 35 },
      xAxis: {
        type: 'category',
        data: ['Q4 2024', 'Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025', 'Q1 2026'],
        axisLabel: { fontSize: fs(11), rotate: isMobile ? 30 : 0 },
        axisLine: { lineStyle: { color: palette.grid } }
      },
      yAxis: { type: 'value', axisLabel: { fontSize: fs(11), formatter: '{value}%' }, splitLine: { lineStyle: { color: palette.grid } } },
      series: [
        { name: '毛利率', type: 'line', data: [72.2, 73.9, 74.8, 75.1, 76.4, 77.5], smooth: true, symbol: 'circle', symbolSize: 6, lineStyle: { width: 2.5 } },
        { name: '营业利润率', type: 'line', data: [5.9, 7.7, 9.9, 11.7, 13.9, 14.2], smooth: true, symbol: 'circle', symbolSize: 6, lineStyle: { width: 2.5 } },
        { name: '净利率', type: 'line', data: [33.0, 6.9, 8.6, 11.0, 13.0, 11.8], smooth: true, symbol: 'circle', symbolSize: 6, lineStyle: { width: 2.5 } },
        { name: 'ROE', type: 'line', data: [6.5, 7.0, 8.2, 10.5, 12.0, 14.5], smooth: true, symbol: 'circle', symbolSize: 6, lineStyle: { width: 2.5 } }
      ]
    });
    window.addEventListener('resize', function() { chart3.resize(); });
  }

  // ============================================================
  // 4. chart-cashflow: 现金流结构（分组柱状图）
  // ============================================================
  var chart4El = document.getElementById('chart-cashflow');
  if (chart4El) {
    var chart4 = echarts.init(chart4El, null, { renderer: 'svg' });
    chart4.setOption({
      animation: false,
      color: [palette.series1, palette.series3, palette.series2],
      tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
      legend: { data: ['经营现金流', '资本支出', '自由现金流'], top: 5, textStyle: { fontSize: fs(12) } },
      grid: { left: isMobile ? '10%' : '8%', right: '5%', top: 50, bottom: 35 },
      xAxis: {
        type: 'category',
        data: ['Q2 2025', 'Q3 2025', 'Q4 2025', 'Q1 2026'],
        axisLabel: { fontSize: fs(11) },
        axisLine: { lineStyle: { color: palette.grid } }
      },
      yAxis: { type: 'value', name: '百万美元', nameTextStyle: { fontSize: fs(11) }, axisLabel: { fontSize: fs(11) }, splitLine: { lineStyle: { color: palette.grid } } },
      series: [
        { name: '经营现金流', type: 'bar', data: [-1467, 73, -991, 119], itemStyle: { color: palette.series1 } },
        { name: '资本支出', type: 'bar', data: [-66, -63, -68, -69], itemStyle: { color: palette.series3 } },
        { name: '自由现金流', type: 'bar', data: [-1533, 10, -1059, 50], itemStyle: { color: palette.series2 } }
      ]
    });
    window.addEventListener('resize', function() { chart4.resize(); });
  }

  // ============================================================
  // 5. chart-kpi-trend: KPI趋势（多折线，双Y轴）
  // ============================================================
  var chart5El = document.getElementById('chart-kpi-trend');
  if (chart5El) {
    var chart5 = echarts.init(chart5El, null, { renderer: 'svg' });
    chart5.setOption({
      animation: false,
      color: [palette.series1, palette.series2, palette.series3],
      tooltip: { trigger: 'axis' },
      legend: { data: ['营收(亿$)', '毛利润(亿$)', '净利润(亿$)'], top: 5, textStyle: { fontSize: fs(12) } },
      grid: { left: isMobile ? '10%' : '8%', right: '5%', top: 50, bottom: 40 },
      xAxis: {
        type: 'category',
        data: ['Q4 2024', 'Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025', 'Q1 2026'],
        axisLabel: { fontSize: fs(11), rotate: isMobile ? 30 : 0 },
        axisLine: { lineStyle: { color: palette.grid } }
      },
      yAxis: { type: 'value', axisLabel: { fontSize: fs(11) }, splitLine: { lineStyle: { color: palette.grid } } },
      series: [
        { name: '营收(亿$)', type: 'line', data: [10.08, 10.37, 11.30, 12.68, 13.35, 14.08], smooth: true, symbol: 'circle', symbolSize: 6, lineStyle: { width: 2.5 } },
        { name: '毛利润(亿$)', type: 'line', data: [7.27, 7.66, 8.45, 9.52, 10.20, 10.91], smooth: true, symbol: 'circle', symbolSize: 6, lineStyle: { width: 2.5 } },
        { name: '净利润(亿$)', type: 'line', data: [3.32, 0.71, 0.97, 1.39, 1.74, 1.67], smooth: true, symbol: 'circle', symbolSize: 6, lineStyle: { width: 2.5 } }
      ]
    });
    window.addEventListener('resize', function() { chart5.resize(); });
  }

  // ============================================================
  // 6. chart-geo: 分部营收占比（饼图）
  // ============================================================
  var chart6El = document.getElementById('chart-geo');
  if (chart6El) {
    var chart6 = echarts.init(chart6El, null, { renderer: 'svg' });
    chart6.setOption({
      animation: false,
      color: [palette.series1, palette.series2, palette.series3],
      tooltip: { trigger: 'item', formatter: '{b}: {c}亿$ ({d}%)' },
      legend: { orient: isMobile ? 'horizontal' : 'vertical', right: isMobile ? 'center' : 10, top: isMobile ? 'bottom' : 'middle', textStyle: { fontSize: fs(12) } },
      series: [{
        name: '分部营收',
        type: 'pie',
        radius: ['40%', '70%'],
        center: isMobile ? ['50%', '42%'] : ['40%', '50%'],
        label: { show: true, formatter: '{b}\n{d}%', fontSize: fs(11) },
        labelLine: { show: true },
        data: [
          { value: 6.85, name: '借贷业务' },
          { value: 3.20, name: '金融服务' },
          { value: 2.15, name: '技术平台' }
        ]
      }]
    });
    window.addEventListener('resize', function() { chart6.resize(); });
  }

  // ============================================================
  // 7. chart-radar: 综合财务指标雷达图
  // ============================================================
  var chart7El = document.getElementById('chart-radar');
  if (chart7El) {
    var chart7 = echarts.init(chart7El, null, { renderer: 'svg' });
    chart7.setOption({
      animation: false,
      color: [palette.series1, palette.series3],
      tooltip: { trigger: 'item' },
      legend: { data: ['Q1 2026', 'Q2 2026'], top: 5, textStyle: { fontSize: fs(12) } },
      radar: {
        indicator: [
          { name: '营收增长', max: 100 },
          { name: '盈利能力', max: 100 },
          { name: '运营效率', max: 100 },
          { name: '财务健康', max: 100 },
          { name: '增长质量', max: 100 },
          { name: '股东回报', max: 100 }
        ],
        radius: isMobile ? '55%' : '65%',
        axisName: { fontSize: fs(11) },
        splitLine: { lineStyle: { color: palette.grid } },
        splitArea: { areaStyle: { color: ['rgba(0,113,227,0.02)', 'rgba(0,113,227,0.05)'] } }
      },
      series: [{
        type: 'radar',
        data: [
          { value: [85, 72, 78, 75, 82, 70], name: 'Q1 2026', areaStyle: { opacity: 0.15 } },
          { value: [92, 78, 82, 76, 88, 75], name: 'Q2 2026', areaStyle: { opacity: 0.2 } }
        ]
      }]
    });
    window.addEventListener('resize', function() { chart7.resize(); });
  }
})();
