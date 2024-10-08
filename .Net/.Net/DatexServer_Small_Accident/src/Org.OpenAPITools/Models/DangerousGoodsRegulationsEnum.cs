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
        /// Gets or Sets DangerousGoodsRegulationsEnum
        /// </summary>
        [TypeConverter(typeof(CustomEnumConverter<DangerousGoodsRegulationsEnum>))]
        [JsonConverter(typeof(Newtonsoft.Json.Converters.StringEnumConverter))]
        public enum DangerousGoodsRegulationsEnum
        {
            
            /// <summary>
            /// Enum AdrEnum for adr
            /// </summary>
            [EnumMember(Value = "adr")]
            AdrEnum = 1,
            
            /// <summary>
            /// Enum IataIcaoEnum for iataIcao
            /// </summary>
            [EnumMember(Value = "iataIcao")]
            IataIcaoEnum = 2,
            
            /// <summary>
            /// Enum ImoImdgEnum for imoImdg
            /// </summary>
            [EnumMember(Value = "imoImdg")]
            ImoImdgEnum = 3,
            
            /// <summary>
            /// Enum RailroadDangerousGoodsBookEnum for railroadDangerousGoodsBook
            /// </summary>
            [EnumMember(Value = "railroadDangerousGoodsBook")]
            RailroadDangerousGoodsBookEnum = 4,
            
            /// <summary>
            /// Enum ExtendedGEnum for extendedG
            /// </summary>
            [EnumMember(Value = "extendedG")]
            ExtendedGEnum = 5
        }
}
