/**
 * Palantir Q2 2026 ECharts Charts
 */
(function () {
  'use strict';
  var rootStyle = getComputedStyle(document.documentElement);
  function cssVar(name, fallback) {
    var v = rootStyle.getPropertyValue(name);
    v = v ? v.trim() : '';
    return v || fallback;
  }
  var P = {
    primary:    cssVar('--accent',         '#2563eb'),
    accent:     cssVar('--accent',         '#2563eb'),
    positive:   cssVar('--accent2',        '#16a34a'),
    negative:   cssVar('--neg',            '#dc2626'),
    neutral:    cssVar('--muted',          '#64748b'),
    text:       cssVar('--ink',            '#1e293b'),
    textMuted:  cssVar('--muted',          '#64748b'),
    grid:       cssVar('--rule',           '#e2e8f0'),
    surface:    cssVar('--bg2',            '#ffffff'),
    s1: '#2563eb', s2: '#16a34a', s3: '#f59e0b', s4: '#8b5cf6', s5: '#ef4444'
  };
  var isMobile = window.innerWidth <= 700;
  function fs(b) { return isMobile ? Math.round(b * 0.86) : b; }
  function makeGrid() {
    return isMobile
      ? { left: 38, right: 16, top: 34, bottom: 58, containLabel: true }
      : { left: 56, right: 28, top: 42, bottom: 48, containLabel: true };
  }
  function axisLabel() { return { color: P.textMuted, fontSize: fs(12) }; }

  /* 1. chart-revenue-trend */
  (function () {
    var el = document.getElementById('chart-revenue-trend');
    if (!el) return;
    var cats = ['24Q4','25Q1','25Q2','25Q3','25Q4','26Q1','26Q2'];
    var revenue = [8.28, 8.84, 10.04, 11.81, 14.07, 16.33, 19.35];
    var netIncome = [0.79, 2.14, 3.27, 4.76, 6.09, 8.71, 10.62];
    var chart = echarts.init(el, null, { renderer: 'svg' });
    chart.setOption({
      animation: false, color: [P.s1, P.s2], grid: makeGrid(),
      legend: { top: 0, textStyle: { color: P.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis' },
      xAxis: { type: 'category', data: cats, axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 45 : 0 }), axisLine: { lineStyle: { color: P.grid } }, axisTick: { show: false } },
      yAxis: [
        { type: 'value', name: '营收(亿美元)', nameTextStyle: { color: P.textMuted, fontSize: fs(11) }, axisLabel: axisLabel(), splitLine: { lineStyle: { color: P.grid } } },
        { type: 'value', name: '净利润(亿美元)', nameTextStyle: { color: P.textMuted, fontSize: fs(11) }, axisLabel: axisLabel(), splitLine: { show: false } }
      ],
      series: [
        { name: '营收', type: 'bar', yAxisIndex: 0, data: revenue, barMaxWidth: isMobile ? 18 : 30, itemStyle: { color: P.s1, borderRadius: [3,3,0,0] } },
        { name: '净利润', type: 'line', yAxisIndex: 1, data: netIncome, smooth: true, symbol: 'circle', symbolSize: isMobile ? 6 : 8, lineStyle: { width: 2, color: P.s2 }, itemStyle: { color: P.s2 } }
      ]
    });
    window.addEventListener('resize', function () { chart.resize(); });
  })();

  /* 2. chart-revenue-mix */
  (function () {
    var el = document.getElementById('chart-revenue-mix');
    if (!el) return;
    var data = [
      { name: '美国政府', value: 8.09 },
      { name: '美国商业', value: 7.64 },
      { name: '国际业务', value: 3.62 }
    ];
    var colors = [P.s1, P.s2, P.s3];
    var lg = isMobile ? { bottom: 0, left: 'center', orient: 'horizontal', textStyle: { color: P.textMuted, fontSize: fs(11) }, itemWidth: fs(10), itemHeight: fs(10) }
      : { top: 'middle', right: 8, orient: 'vertical', textStyle: { color: P.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) };
    var chart = echarts.init(el, null, { renderer: 'svg' });
    chart.setOption({
      animation: false, color: colors, legend: lg,
      tooltip: { trigger: 'item', formatter: '{b}: ${c}亿 ({d}%)' },
      series: [{ type: 'pie', radius: isMobile ? ['38%','62%'] : ['52%','72%'], center: isMobile ? ['50%','42%'] : ['38%','50%'],
        avoidLabelOverlap: true,
        itemStyle: { borderColor: P.surface, borderWidth: 2 },
        label: { color: P.text, fontSize: fs(12), formatter: '{d}%' },
        labelLine: { lineStyle: { color: P.grid } },
        data: data
      }]
    });
    window.addEventListener('resize', function () { chart.resize(); });
  })();

  /* 3. chart-margin-trend */
  (function () {
    var el = document.getElementById('chart-margin-trend');
    if (!el) return;
    var cats = ['24Q4','25Q1','25Q2','25Q3','25Q4','26Q1','26Q2'];
    var grossMargin = [78.9, 80.4, 80.8, 82.4, 84.6, 86.8, 84.7];
    var operatingMargin = [1.3, 19.9, 26.8, 33.3, 40.9, 46.2, 47.0];
    var netMargin = [9.5, 24.2, 32.6, 40.3, 43.3, 53.3, 54.9];
    var chart = echarts.init(el, null, { renderer: 'svg' });
    chart.setOption({
      animation: false, color: [P.s1, P.s3, P.s2], grid: makeGrid(),
      legend: { top: 0, textStyle: { color: P.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis', valueFormatter: function(v){ return v + '%'; } },
      xAxis: { type: 'category', data: cats, axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 45 : 0 }), axisLine: { lineStyle: { color: P.grid } }, axisTick: { show: false } },
      yAxis: { type: 'value', name: '百分比(%)', nameTextStyle: { color: P.textMuted, fontSize: fs(11) }, axisLabel: axisLabel(), splitLine: { lineStyle: { color: P.grid } }, min: 0, max: 100 },
      series: [
        { name: '毛利率', type: 'line', data: grossMargin, smooth: true, symbol: 'circle', symbolSize: isMobile ? 5 : 7, lineStyle: { width: 2 }, itemStyle: { color: P.s1 } },
        { name: '营业利润率', type: 'line', data: operatingMargin, smooth: true, symbol: 'circle', symbolSize: isMobile ? 5 : 7, lineStyle: { width: 2 }, itemStyle: { color: P.s3 } },
        { name: '净利率', type: 'line', data: netMargin, smooth: true, symbol: 'circle', symbolSize: isMobile ? 5 : 7, lineStyle: { width: 2 }, itemStyle: { color: P.s2 } }
      ]
    });
    window.addEventListener('resize', function () { chart.resize(); });
  })();

  /* 4. chart-cashflow */
  (function () {
    var el = document.getElementById('chart-cashflow');
    if (!el) return;
    var cats = ['25Q2','25Q3','25Q4','26Q1','26Q2'];
    var ocf = [5.38, 5.08, 7.77, 8.99, 12.16];
    var capex = [0.08, 0.07, 0.13, 0.07, 0.04];
    var fcf = [5.31, 5.01, 7.64, 8.92, 12.20];
    var chart = echarts.init(el, null, { renderer: 'svg' });
    chart.setOption({
      animation: false, color: [P.s1, P.s5, P.s2], grid: makeGrid(),
      legend: { top: 0, textStyle: { color: P.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis' },
      xAxis: { type: 'category', data: cats, axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 45 : 0 }), axisLine: { lineStyle: { color: P.grid } }, axisTick: { show: false } },
      yAxis: { type: 'value', name: '亿美元', nameTextStyle: { color: P.textMuted, fontSize: fs(11) }, axisLabel: axisLabel(), splitLine: { lineStyle: { color: P.grid } } },
      series: [
        { name: '经营现金流', type: 'bar', data: ocf, barMaxWidth: isMobile ? 18 : 28, itemStyle: { color: P.s1, borderRadius: [3,3,0,0] } },
        { name: '资本支出', type: 'bar', data: capex, barMaxWidth: isMobile ? 18 : 28, itemStyle: { color: P.s5, borderRadius: [3,3,0,0] } },
        { name: '自由现金流', type: 'line', data: fcf, smooth: true, symbol: 'circle', symbolSize: isMobile ? 6 : 8, lineStyle: { width: 2, color: P.s2 }, itemStyle: { color: P.s2 } }
      ]
    });
    window.addEventListener('resize', function () { chart.resize(); });
  })();

  /* 5. chart-kpi-trend */
  (function () {
    var el = document.getElementById('chart-kpi-trend');
    if (!el) return;
    var cats = ['25Q2','25Q3','25Q4','26Q1','26Q2'];
    var tcv = [22.64, 24.50, 28.00, 31.00, 33.73];
    var largeContracts = [139, 154, 179, 199, 220];
    var chart = echarts.init(el, null, { renderer: 'svg' });
    chart.setOption({
      animation: false, color: [P.s1, P.s3], grid: makeGrid(),
      legend: { top: 0, textStyle: { color: P.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: { trigger: 'axis' },
      xAxis: { type: 'category', data: cats, axisLabel: Object.assign({}, axisLabel(), { rotate: isMobile ? 45 : 0 }), axisLine: { lineStyle: { color: P.grid } }, axisTick: { show: false } },
      yAxis: [
        { type: 'value', name: 'TCV(亿美元)', nameTextStyle: { color: P.textMuted, fontSize: fs(11) }, axisLabel: axisLabel(), splitLine: { lineStyle: { color: P.grid } } },
        { type: 'value', name: '大额合同数', nameTextStyle: { color: P.textMuted, fontSize: fs(11) }, axisLabel: axisLabel(), splitLine: { show: false } }
      ],
      series: [
        { name: '总合同价值', type: 'bar', yAxisIndex: 0, data: tcv, barMaxWidth: isMobile ? 18 : 28, itemStyle: { color: P.s1, borderRadius: [3,3,0,0] } },
        { name: '百万美元+合同数', type: 'line', yAxisIndex: 1, data: largeContracts, smooth: true, symbol: 'circle', symbolSize: isMobile ? 6 : 8, lineStyle: { width: 2, color: P.s3 }, itemStyle: { color: P.s3 } }
      ]
    });
    window.addEventListener('resize', function () { chart.resize(); });
  })();

  /* 6. chart-geo */
  (function () {
    var el = document.getElementById('chart-geo');
    if (!el) return;
    var data = [
      { name: '美国政府', value: 8.09 },
      { name: '美国商业', value: 7.64 },
      { name: '国际业务', value: 3.62 }
    ];
    var colors = [P.s1, P.s2, P.s3];
    var lg = isMobile ? { bottom: 0, left: 'center', orient: 'horizontal', textStyle: { color: P.textMuted, fontSize: fs(11) }, itemWidth: fs(10), itemHeight: fs(10) }
      : { top: 'middle', right: 8, orient: 'vertical', textStyle: { color: P.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) };
    var chart = echarts.init(el, null, { renderer: 'svg' });
    chart.setOption({
      animation: false, color: colors, legend: lg,
      tooltip: { trigger: 'item', formatter: '{b}: ${c}亿 ({d}%)' },
      series: [{ type: 'pie', radius: isMobile ? ['38%','62%'] : ['52%','72%'], center: isMobile ? ['50%','42%'] : ['38%','50%'],
        avoidLabelOverlap: true,
        itemStyle: { borderColor: P.surface, borderWidth: 2 },
        label: { color: P.text, fontSize: fs(12), formatter: '{d}%' },
        labelLine: { lineStyle: { color: P.grid } },
        data: data
      }]
    });
    window.addEventListener('resize', function () { chart.resize(); });
  })();

  /* 7. chart-radar */
  (function () {
    var el = document.getElementById('chart-radar');
    if (!el) return;
    var chart = echarts.init(el, null, { renderer: 'svg' });
    chart.setOption({
      animation: false, color: [P.s1, P.s3],
      legend: { top: 0, textStyle: { color: P.textMuted, fontSize: fs(12) }, itemWidth: fs(12), itemHeight: fs(12) },
      tooltip: {},
      radar: {
        indicator: [
          { name: '营收增长', max: 100 },
          { name: '盈利能力', max: 100 },
          { name: '现金流', max: 100 },
          { name: '运营效率', max: 100 },
          { name: '资产负债', max: 100 },
          { name: '估值合理性', max: 100 }
        ],
        axisName: { color: P.textMuted, fontSize: fs(12) },
        splitLine: { lineStyle: { color: P.grid } },
        splitArea: { areaStyle: { color: [P.surface, 'rgba(0,0,0,0.02)'] } },
        axisLine: { lineStyle: { color: P.grid } }
      },
      series: [{
        type: 'radar',
        data: [
          { name: 'Palantir Q2 2026', value: [93, 85, 90, 88, 92, 45], areaStyle: { color: 'rgba(37, 99, 235, 0.2)' }, lineStyle: { color: P.s1, width: 2 }, itemStyle: { color: P.s1 } },
          { name: 'SaaS行业均值', value: [40, 50, 55, 50, 60, 65], areaStyle: { color: 'rgba(245, 158, 11, 0.15)' }, lineStyle: { color: P.s3, width: 2 }, itemStyle: { color: P.s3 } }
        ]
      }]
    });
    window.addEventListener('resize', function () { chart.resize(); });
  })();

})();
