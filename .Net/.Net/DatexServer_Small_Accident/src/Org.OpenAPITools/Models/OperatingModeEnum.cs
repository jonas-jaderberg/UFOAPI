/*
 * DATEX II Snapshot Pull API
 *
 * This is DATEX II Snapshot PULL API returning PayloadPublication.
 *
 * The version of the OpenAPI document: 1.0.2
 * Contact: you@your-company.com
 * Generated by: https://openapi-generator.tech
 */

using System;
using System.Linq;
using System.Text;
using System.Collections.Generic;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Org.OpenAPITools.Converters;

namespace Org.OpenAPITools.Models
{ 
        /// <summary>
        /// Gets or Sets OperatingModeEnum
        /// </summary>
        [TypeConverter(typeof(CustomEnumConverter<OperatingModeEnum>))]
        [JsonConverter(typeof(Newtonsoft.Json.Converters.StringEnumConverter))]
        public enum OperatingModeEnum
        {
            
            /// <summary>
            /// Enum ConditionTriggeredEnum for conditionTriggered
            /// </summary>
            [EnumMember(Value = "conditionTriggered")]
            ConditionTriggeredEnum = 1,
            
            /// <summary>
            /// Enum OnOccurrenceEnum for onOccurrence
            /// </summary>
            [EnumMember(Value = "onOccurrence")]
            OnOccurrenceEnum = 2,
            
            /// <summary>
            /// Enum OtherEnum for other
            /// </summary>
            [EnumMember(Value = "other")]
            OtherEnum = 3,
            
            /// <summary>
            /// Enum PeriodicEnum for periodic
            /// </summary>
            [EnumMember(Value = "periodic")]
            PeriodicEnum = 4,
            
            /// <summary>
            /// Enum ExtendedGEnum for extendedG
            /// </summary>
            [EnumMember(Value = "extendedG")]
            ExtendedGEnum = 5
        }
}
